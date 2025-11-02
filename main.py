from fastapi import FastAPI
from database import engine, Base
from routers import tasks  # import router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-Do List API with MySQL")

# Include router
app.include_router(tasks.router)
