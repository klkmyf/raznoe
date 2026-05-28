from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "userss"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    
    
class Flight(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, index=True)
    airline = Column(String, index=True)
    price = Column(Float,  index=True) 
    available_seats = Column(Integer,  index=True)
    bookings = relationship("Booking", back_populates="flight", cascade="all, delete-orphan")
    


class Booking(Base):
    __tablename__ = "bookings" 
    id = Column(Integer, primary_key=True, index=True)
    passenger_name = Column(String, index=True)
    booking_date = Column(DateTime, index=True) 
    flight_id = Column(Integer, ForeignKey("flights.id", ondelete="CASCADE"), nullable=False)
    flight = relationship("Flight", back_populates="bookings") 
