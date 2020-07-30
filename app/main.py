from fastapi import FastAPI

from app.router import expense, travel_expense, trip


app = FastAPI()


app.include_router(expense.router)
app.include_router(travel_expense.router)
app.include_router(trip.router)