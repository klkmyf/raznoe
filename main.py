from fastapi import FastAPI, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db
from services.user_service import get_all_users
from services.flights_service import get_all_bookings
from services.flights_service import create_new_booking
from services.flights_service import get_all_flights
from services.flights_service import create_flight

from models.schema import UserCreate
from models.schema import BookingCreate
from services.user_service import create_user
from services.flights_service import FlightCreate
from pydantic import BaseModel
from datetime import datetime


app = FastAPI()


@app.get("/userss/")
async def read_users(db: AsyncSession = Depends(get_db)):
    users = await get_all_users(db)
    return users

@app.post("/userss/")
async def add_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    created_user = await create_user(db, user)
    return created_user




@app.get("/bookings/")
async def read_bookings(db: AsyncSession = Depends(get_db)):
    bookings = await get_all_bookings(db)
    return bookings

@app.post("/bookings/", status_code=status.HTTP_201_CREATED)
async def add_booking(booking_data: BookingCreate, db: AsyncSession = Depends(get_db)):
    new_booking = await create_new_booking(db, booking_data)
    return new_booking




@app.post("/fligts/", status_code=status.HTTP_201_CREATED)
async def add_flight(flight_data: FlightCreate, db: AsyncSession = Depends(get_db)):
    created_flight = await create_flight(db, flight_data)
    return created_flight

@app.get("/flights/")
async def read_flights(db: AsyncSession = Depends(get_db)):
    all_flights = await get_all_flights(db)
    return all_flights

