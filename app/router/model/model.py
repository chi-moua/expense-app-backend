from pydantic import BaseModel

from app.database.model.enum import ExpenseType


class ExpenseCreate(BaseModel):
    '''Represents a pydantic model that handles the create expense request.'''
    date: str
    amount: float
    business: str
    expense_type: ExpenseType
    description: str = None

class Expense(ExpenseCreate):
    '''Model that handles the expense request.'''
    expense_id = int
    
    class Config:
        orm_mode = True


class TripCreate(BaseModel):
    '''Represents a pydantic model that handles the trip request.'''
    name: str
    start_date: str
    end_date: str
    description: str


class Trip(TripCreate):
    '''Model that handles the trip request.'''
    trip_id = int

    class Config:
        orm_mode = True


class TravelExpenseCreate(BaseModel):
    '''Represents a pydantic model that handles the travel expense request.'''
    expense: ExpenseCreate 
    trip_id: int
    

class TravelExpense(BaseModel):
    '''Model that handles the travel expense request.'''
    travel_expense_id: int
    trip_id: int
    expense: Expense
    



