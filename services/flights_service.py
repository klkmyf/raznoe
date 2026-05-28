from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from datetime import datetime
from models.model import Flight, Booking
from models.schema import FlightCreate, BookingCreate
from fastapi import HTTPException, status


async def get_all_flights(db: AsyncSession):
    selfli = select(Flight)
    result = await db.execute(selfli)
    return result.scalars().all()


async def get_all_bookings(db: AsyncSession):
    selbook = select(Booking)
    result = await db.execute(selbook)
    return result.scalars().all()



async def create_flight(db: AsyncSession, flight_data):
    new_flight = Flight(flight_number=flight_data.flight_number, airline=flight_data.airline, price=flight_data.price, available_seats=flight_data.available_seats)
    db.add(new_flight)
    await db.commit()
    await db.refresh(new_flight)
    return new_flight



async def create_new_booking(db: AsyncSession, booking_data: BookingCreate):
    
    query = select(Flight).where(Flight.id == booking_data.flight_id)
    result = await db.execute(query)
    flight = result.scalar_one_or_none()
    
    if not flight:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Такого рейса нет")
        
    if flight.available_seats <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Свободных мест на данный рейс нет, выберите другой вариант")
    
    
    flight.available_seats -= 1
    
    new_booking = Booking(passenger_name=booking_data.passenger_name, booking_date=booking_data.booking_date, flight_id=booking_data.flight_id)
    
    db.add(new_booking)
    
    await db.commit()
    await db.refresh(new_booking)
    
    return new_booking
