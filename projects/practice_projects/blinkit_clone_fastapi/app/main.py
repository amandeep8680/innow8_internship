from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from contextlib import asynccontextmanager
from app.database.database import engine
from app.routes.user_routes import router as user_routes
## testing database connection
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("✅ Database connected successfully!")
    except SQLAlchemyError as e:
        print(f"❌ Database connection failed: {e}")

    yield

## creating instance of the app
app = FastAPI(
    title="Blinkit API's",
    lifespan=lifespan
)

app.include_router(user_routes)