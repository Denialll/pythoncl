from sqlalchemy import Column, Integer, Date, ForeignKey, String

from database import Base


class Practises(Base):
    __tablename__ = "practice"
    id = Column(Integer, primary_key=True)
    file_name = Column(String)
    link = Column(String)
    year = Column(Integer, nullable=False)
