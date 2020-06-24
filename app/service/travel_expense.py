from typing import List

from app.database.dao.travel_expense import TravelExpenseDao
from app.service.expense import ExpenseService
from app.service.trip import TripService
from app.router.model import model
from app.database.model import schema
from app.util.transform import ModelTransformManager


class TravelExpenseService:
    '''The Trip Service contains the business logic layer for the Trip related data.'''

    def __init__(self):
        self.travelExpenseDao = TravelExpenseDao.get_dao()
        self.expenseService = ExpenseService.get_service()
        self.tripService = TripService.get_service()


    def create_travel_expense(
        self,
        travel_expense: model.TravelExpenseCreate) -> schema.TravelExpense:
        '''Adds the travel expense to the database with related expense and trip information.

        :param travel_expense: The travel expense
        :type travel_expense: router.model.model.TravelExpenseCreate
        :type expense: database.model.schema.Expense
        :return: The travel expense
        :rtype: database.model.schema.TravelExpense
        '''
        db_expense = ModelTransformManager \
            .model_expense_create_to_schema(travel_expense.expense)
        self.expenseService.create_expense(db_expense)
        db_travel_expense = ModelTransformManager \
            .travel_expense_create_to_schema(
                db_expense.expense_id,
                travel_expense.trip_id
            )
        return self.travelExpenseDao \
            .create_travel_expense(db_expense, db_travel_expense)

