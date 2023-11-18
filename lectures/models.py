from sqlalchemy import Column, Integer, Date, String
from database import Base

class Lectures(Base):
    __tablename__ = "lecture"
    id = Column(Integer, primary_key=True)
    file_name = Column(String)
    link = Column(String)
    year = Column(Integer, nullable=False)