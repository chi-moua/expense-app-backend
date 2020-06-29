from fastapi import APIRouter

from app.service.expense import ExpenseService
from app.router.model.model import ExpenseCreate, Expense


router = APIRouter()


@router.post('/expense/', tags=['expense'])
def create_expense(expense: ExpenseCreate):
    expense = ExpenseService.get_service()\
        .create_expense(expense)
    return expense


@router.get('/expense/{expense_id}', tags=['expense'])
def get_expense_by_id(expense_id: int):
    expense = ExpenseService.get_service()\
        .get_expense_by_id(expense_id)
    return expense


@router.get('/expense', tags=['expense'])
def get_all_expense():
    expenses = ExpenseService.get_service()\
        .get_all_expense()
    return expenses


@router.put('/expense', tags['expense'])
def update_expense(expense: Expense):
    ExpenseService.get_service()\
        .update_expense(expense)
    return


@router.delete('/expense/{expense_id}')
def delete_expense(expense_id: int):
    ExpenseService.get_service()\
        .delete_expense_by_id(expense_id)
    return
