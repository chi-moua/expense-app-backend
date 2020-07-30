from fastapi import APIRouter

from app.service.travel_expense import TravelExpenseService
from app.router.model.model import TravelExpenseCreate, TravelExpense


TAG = ['travel expense']

router = APIRouter()

@router.post('/travelexpense', tags=TAG)
def create_travel_expense(travel_expense: TravelExpenseCreate):
    res_expense = TravelExpenseService.get_service()\
        .create_travel_expense(travel_expense)
    return res_expense


@router.get('/travelexpense/{expense_id}', tags=TAG)
def get_travel_expense_by_id(expense_id: int):
    res_expense = TravelExpenseService.get_service()\
        .get_travel_expense_by_id(expense_id)
    return res_expense


@router.put('/travelexpense', tags=TAG)
def update_travel_expense(expense: TravelExpense):
    TravelExpenseService.get_service()\
        .update_expense(expense)
    return


@router.delete('/travelexpense/{travel_expense_id}', tags=TAG)
def delete_travel_expense(travel_expense_id: int):
    TravelExpenseService.get_service()\
        .delete_travel_expense(travel_expense_id)
    return