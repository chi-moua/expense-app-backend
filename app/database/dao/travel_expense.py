from app.database.connection import DBConnectionManager
from app.database.model.schema import TravelExpense, Expense
from app.database.dao.expense import ExpenseDao


class TravelExpenseDao:
    '''The Travel Expense Dao contains CRUD functionality that interacts with the database.'''

    def __init__(self):
        self.db = DBConnectionManager.get_db()
        self.expenseDao = ExpenseDao.get_dao()
    
    @classmethod
    def get_dao(cls):
        '''Gets an instance of the Travel Expense Dao.

        :return: The travel_expense Dao
        :rtype: travel_expenseDao
        '''
        return cls()


    def create_travel_expense(
        self, 
        expense: Expense, 
        travel_expense: TravelExpense):
        '''Adds the travel expense to the database.

        :param travel_expense: The travel expense
        :type travel_expense: database.model.schema.TravelExpense
        :return: The travel expense
        :rtype: database.model.schema.TravelExpense
        '''
        db_expense = self.expenseDao.create_expense(expense)
        self.db.add(travel_expense)
        self.db.commit()
        return db_expense, travel_expense


    def get_travel_expense_by_id(self, travel_expense_id: int):
        '''Gets the travel expense with the given id.

        :param travel_expense_id: The travel expense id.
        :type travel_expense_id: Integer
        :return: The travel expense
        :rtype: database.model.schema.TravelExpense
        '''
        db_travel_expense = self.db.query(TravelExpense)\
            .filter(_id == travel_expense_id)\
                .join(Expense, Expense._id == TravelExpense._id).first()
        return db_travel_expense         


    def get_all_travel_expenses(self):
        '''Gets all the travel expenses.

        :return: The travel expenses
        :rtype: List[database.model.schema.TravelExpense]
        '''
        return self.db.query(TravelExpense)\
            .join(Expense, Expense._id == TravelExpense._id).all()


    def update_travel_expense(
        self, 
        travel_expense: TravelExpense, 
        expense: Expense):
        '''Updates the given travel_expense to the database.
        
        :param travel_expense: The travel expense
        :param updates: The updates
        :type travel_expense: database.model.schema.TravelExpense
        :type updates: Dictionary
        :return: The travel expense
        :rtype: database.model.schema.TravelExpense
        '''
        self.db.commit()
        return expense, travel_expense
    

    def delete_travel_expense(self, travel_expense: TravelExpense):
        '''Deletes the given travel expense in the database.

        :param travel_expense: The travel expense
        :type travel_expense: database.model.schema.TravelExpense
        '''
        self.db.delete(travel_expense)
        self.db.commit()
        