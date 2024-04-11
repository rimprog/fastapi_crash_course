from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_tables, delete_tables
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('Database tables deleted')
    await create_tables()
    print('Database tables created')
    yield
    print('Shutdown completing')


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
