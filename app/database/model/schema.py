from sqlalchemy.types import Column, Integer, String, \
    Date, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.database.connection.DBConnectionManager import Base
from app.database.schema.enum import ExpenseType


class Expense(Base):
    '''Expense ORM model that correlates to the expense table in the database.'''
    __tablename__ = 'expense'

    _id = Column('id', Integer, primary_key=True)
    date = Column('date', Date)
    amount = Column('dollar_amount', Float)
    business = Column('business', String)
    expense_type = Column('type', Enum(ExpenseType))
    description = Column('description', String(50))


class Trip(Base):
    '''Trip ORM model that correlates to the trip table in the database.'''
    __tablename__ = 'trip'

    _id = Column('id', Integer, primary_key=True)
    name = Column('name', String(50))
    start_date = Column('start_date', Date)
    end_date = Column('end_date', Date)
    description = Column('description', String(50))


class TravelExpense(Base):
    '''Travel Expense ORM model that correlates to the travel expense table in the database.'''
    __tablename__ = 'travel_expense'

    _id = Column('id', Integer, primary_key=True)
    expense_id = Column('expense_id', ForeignKey('expense.id'))
    trip_id = Column('trip_id', ForeignKey('trip.id'))
    expense = relationship('Expense')
    trip = relationship('Trip')
    
