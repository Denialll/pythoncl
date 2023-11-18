from sqlalchemy import Column, Integer, Date, String, select

from dao.base import BaseDAO
from database import async_session_maker
from tasks.models import Tasks


class TasksDAO(BaseDAO):
    model = Tasks