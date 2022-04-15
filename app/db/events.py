from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlmodel import SQLModel
from starlite import State

from app.core.config import settings
from app.models.schemas import users as users


async def create_db_engine(state: State) -> None:
    state.pool = create_async_engine(
        settings.database_url, **settings.sqlalchemy_kwargs
    )


async def dispose_db_engine(state: State) -> None:
    await state.pool.dispose()


async def create_db_tables(state: State) -> None:
    if isinstance(state.pool, AsyncEngine):
        async with state.pool.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
    else:
        raise TypeError(
            "sqlalchemy.ext.asyncio.engine.AsyncEngine missing from app state."
        )
