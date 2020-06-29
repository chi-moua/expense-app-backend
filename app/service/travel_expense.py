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
            .create_travel_expense(db_travel_expense)


    def get_travel_expense_by_id(self, travel_expense_id: int):
        '''Gets the travel expense with the given id.

        :param travel_expense_id: The travel expense id.
        :type travel_expense_id: Integer
        :return: The travel expense
        :rtype: database.model.schema.TravelExpense
        '''
        return self.travelExpenseDao\
            .get_travel_expense_by_id(travel_expense_id)


    def update_travel_expense(self, travel_expense: model.TravelExpense):
        '''Updates the given travel_expense to the database.
        
        :param travel_expense: The travel expense
        :type travel_expense: router.model.model.TravelExpense
        '''
        self.expenseService.update_expense(travel_expense.expense)
        return

    
    def delete_travel_expense(self, travel_expense: TravelExpense):
        '''Deletes the given travel expense in the database.

        :param travel_expense: The travel expense
        :type travel_expense: router.model.router.TravelExpense
        '''
        self.travelExpenseDao.delete_travel_expense_by_id(travel_expense._id)
        return
    

