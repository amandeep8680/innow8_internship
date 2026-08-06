from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from contextlib import asynccontextmanager
from app.database.database import engine
from app.routes.user_routes import router as user_routes 
from app.routes.branchmanager_routes import router as branchmanager_routes
from app.routes.branches import router as branches 


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
    # lifespan=lifespan     ## Initializes app resources (e.g., database connection) on startup.
)

app.include_router(user_routes)
app.include_router(branchmanager_routes)
app.include_router(branches)