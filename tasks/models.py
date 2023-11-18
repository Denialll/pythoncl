from sqlalchemy import Column, Integer, Date, String

from database import Base


class Tasks(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    deadline = Column(String, nullable=False)
    file_name = Column(String)
    link = Column(String)

