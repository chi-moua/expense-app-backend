
from app.database.connection import DBConnectionManager
from app.database.model.schema import Expense


class ExpenseDao:
    '''The Expense Dao contains CRUD functionality that interacts with the database.'''

    def __init__(self):
        self.db = DBConnectionManager.get_db()

    
    @classmethod
    def get_dao(cls):
        '''Gets an instance of the Expense Dao.

        :return: The Expense Dao
        :rtype: ExpenseDao
        '''
        return cls()


    def create_expense(expense: Expense):
        '''Adds the expense to the database.

        :param expense: The expense
        :type expense: database.model.schema.Expense
        :return: The expense
        :rtype: database.model.schema.Expense
        '''
        self.db.add(expense)
        self.db.commit()
        return expense


    def get_expense_by_id(expense_id: int):
        '''Gets the expense with the given id.

        :param expense_id: The expense id.
        :type expense_id: Integer
        :return: The expense
        :rtype: database.model.schema.Expense
        '''
        return self.db.query(Expense).get(expense_id)


    def get_all_expenses():
        '''Gets all the expenses.

        :return: The expenses
        :rtype: List[database.model.schema.Expense]
        '''
        return self.db.query(Expense).all()


    def update_expense(expense: Expense):
        '''Updates the given expense to the database.
        
        :param expense: The expense
        :type expense: database.model.schema.Expense
        :type updates: Dictionary
        :return: The expense
        :rtype: database.model.schema.Expense
        '''
        self.db.commit()
        return expense
    

    def delete_expense(expense: Expense):
        '''Deletes the given expense in the database.

        :param expense: The expense
        :type expense: database.model.schema.Expense
        '''
        self.db.delete(expense)
        self.db.commit()