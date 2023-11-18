from sqlalchemy import Column, Integer, Date, ForeignKey, String

from database import Base


class Questions(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True)
    file_name = Column(String)
    link = Column(String)
