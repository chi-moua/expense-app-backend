from app.database.connection import DBConnectionManager
from app.database.model.schema import TravelExpense, Expense
from app.database.dao.expense import ExpenseDao


class TravelExpenseDao:
    '''The Travel Expense Dao contains CRUD functionality that interacts with the database.'''

    def __init__(self):
        self.db = DBConnectionManager.get_db()
    

    @classmethod
    def get_dao(cls):
        '''Gets an instance of the Travel Expense Dao.

        :return: The travel_expense Dao
        :rtype: travel_expenseDao
        '''
        return cls()


    def create_travel_expense(
        self, 
        travel_expense: TravelExpense):
        '''Adds the travel expense to the database.

        :param travel_expense: The travel expense
        :type travel_expense: database.model.schema.TravelExpense
        :return: The travel expense
        :rtype: database.model.schema.TravelExpense
        '''
        self.db.add(travel_expense)
        self.db.commit()
        return travel_expense


    def get_travel_expense_by_id(self, travel_expense_id: int):
        '''Gets the travel expense with the given id.

        :param travel_expense_id: The travel expense id.
        :type travel_expense_id: Integer
        :return: The travel expense
        :rtype: database.model.schema.TravelExpense
        '''
        db_travel_expense = self.db.query(TravelExpense)\
            .filter(TravelExpense._id == travel_expense_id)\
                .join(Expense, Expense._id == TravelExpense.expense_id).first()
        return db_travel_expense         


    def get_all_travel_expenses(self):
        '''Gets all the travel expenses.

        :return: The travel expenses
        :rtype: List[database.model.schema.TravelExpense]
        '''
        return self.db.query(TravelExpense)\
            .join(Expense, Expense._id == TravelExpense.expense_id).all()


    def update_travel_expense(
        self, 
        travel_expense: TravelExpense):
        '''Updates the given travel_expense to the database.
        
        :param travel_expense: The travel expense
        :type travel_expense: database.model.schema.TravelExpense
        :return: The travel expense
        :rtype: database.model.schema.TravelExpense
        '''
        self.db.commit()
        return travel_expense
    

    def delete_travel_expense(self, travel_expense: TravelExpense):
        '''Deletes the given travel expense in the database.

        :param travel_expense: The travel expense
        :type travel_expense: database.model.schema.TravelExpense
        '''
        self.db.delete(travel_expense)
        self.db.commit()

    
    def delete_travel_expense_by_id(self, travel_expense_id: int):
        '''Deletes the given travel expense with the id in the database.

        :param travel_expense_id: The travel expense id
        :type travel_expense_id: int
        '''
        self.db.query(TravelExpense)\
            .filter(TravelExpense._id == travel_expense_id)\
                .delete()