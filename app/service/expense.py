from typing import List

from app.database.dao.expense import ExpenseDao
from app.router.model import model
from app.database.model import schema
from app.util.transform import ModelTransformManager


class ExpenseService:
    '''The Expense Service contains the business logic layer for the Expense related data.'''

    def __init__(self):
        self.expenseDao = ExpenseDao.get_dao()

    
    @classmethod
    def get_service(cls):
        '''Gets an instance of the Expense Service.

        :return: The Expense Service
        :rtype: ExpenseService
        '''
        return cls()


    def create_expense(expense: model.ExpenseCreate) -> schema.Expense:
        '''Adds the expense to the database.

        :param expense: The expense
        :type expense: router.model.model.ExpenseCreate
        :return: The expense
        :rtype: database.model.schema.Expense
        '''
        db_expense = ModelTransformManager \
            .model_expense_create_to_schema(expense)
        db_expense = self.expenseDao.create_expense(db_expense)
        return db_expense


    def get_expense_by_id(expense_id: int) -> schema.Expense:
        '''Gets the expense with the given id.

        :param expense_id: The expense id.
        :type expense_id: Integer
        :return: The expense
        :rtype: database.model.schema.Expense
        '''
        return self.expenseDao.get_expense_by_id(expense_id)


    def get_all_expense() -> List[schema.Expense]:
        '''Gets all the expenses.

        :return: The expenses
        :rtype: List[database.model.schema.Expense]
        '''
        return self.expenseDao.get_all_expense()


    def update_expense(expense: model.Expense) -> schema.Expense:
        '''Updates the given expense to the database.
        
        :param expense: The expense
        :type expense: router.model.model.ExpenseCreate
        :type updates: Dictionary
        :return: The expense
        :rtype: database.model.schema.Expense
        '''
        db_expense = ModelTransformManager \
            .model_expense_to_schema(expense)
        db_expense = self.expenseDao.update_expense(db_expense)
        return db_expense

    
    def delete_expense(expense: model.Expense) -> None:
        '''Deletes the given expense in the database.

        :param expense: The expense
        :type expense: router.model.model.ExpenseCreate
        '''
        db_expense = ModelTransformManager \
            .model_expense_to_schema(expense)
        self.expenseDao.delete_expense(expense)
