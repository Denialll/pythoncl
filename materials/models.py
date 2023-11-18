from sqlalchemy import Column, Integer, Date, String
from database import Base

class Materials(Base):
    __tablename__ = "material"
    id = Column(Integer, primary_key=True)
    file_name = Column(String)
    link = Column(String)
    task_id = Column(Integer, nullable=False)