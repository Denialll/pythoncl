from sqlalchemy import select

from database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_files(cls,one=True, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.file_name, cls.model.link).filter_by(**filter_by)
            result = await session.execute(query)
            if one:
                return result.mappings().one()
            else:
                return result.mappings().all()