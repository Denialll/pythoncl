from sqlalchemy import select

from dao.base import BaseDAO
from database import async_session_maker
from lectures.models import Lectures


class LecturesDAO(BaseDAO):
    model = Lectures

