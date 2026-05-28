
from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    
    
class FlightCreate(BaseModel):
    flight_number: str
    airline: str
    price: float 
    available_seats: int
    
  
class BookingCreate(BaseModel):
    passenger_name: str
    flight_id: int
    booking_date: datetime
    
    
