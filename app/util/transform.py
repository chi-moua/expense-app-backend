from app.router.model import model
from app.database.model import schema


class ModelTransformManager:
    '''This class deals with the "translation" of pydantic models to SQL Alchemy schema models and vice versa.
    '''


    @staticmethod
    def model_expense_create_to_schema(
        expense_create: model.ExpenseCreate) -> schema.Expense:
        '''Returns a schema.Expense version of the created expense.

        :param expense_create: The expense to create
        :type expense_create: model.ExpenseCreate
        :return: The schema model of the expense
        :rtype: schema.Expense
        '''
        db_expense = schema.Expense(
            date=expense_create.date,
            amount=expense_create.amount,
            business=expense_create.business,
            expense_type=expense_create.expense_type,
            description=expense_create.description,
            travel_expense=expense_create.travel_expense
        )
        return db_expense


    @staticmethod
    def model_expense_to_schema(expense: model.Expense) -> schema.Expense:
        '''Returns a schema.Expense version of the expense.

        :param expense: The expense
        :type expense: model.ExpenseCreate
        :return: The schema model of the expense
        :rtype: schema.Expense
        '''
        db_expense = schema.Expense(
            _id=expense.expense_id
            date=expense.date,
            amount=expense.amount,
            business=expense.business,
            expense_type=expense.expense_type,
            description=expense.description,
            travel_expense=expense.travel_expense
        )
        return db_expense

    
    @staticmethod
    def model_trip_create_to_schema(
        trip_create: model.TripCreate) ->  schema.Trip:
        '''Returns a schema.Trip version of the created trip.

        :param trip_create: The trip to create
        :type trip_create: model.TripCreate
        :return: The schema model of the trip
        :rtype: schema.Trip
        '''
        db_trip = schema.Trip(
            name=trip_create.name,
            start_date=trip_create.start_date,
            end_date=trip_create.end_date,
            description=trip_create.description
        )
        return db_trip


    @staticmethod
    def model_trip_to_schema(trip: model.Trip) -> schema.Trip:
         '''Returns a schema.Trip version of the trip.

        :param trip: The trip
        :type trip: model.Trip
        :return: The schema model of the trip
        :rtype: schema.Trip
        '''
        db_trip = schema.Trip(
            _id=trip.trip_id,
            name=trip_create.name,
            start_date=trip_create.start_date,
            end_date=trip_create.end_date,
            description=trip_create.description
        )
        return db_trip


    @staticmethod
    def model_travel_expense_create_to_schema(
        travel_expense_create: model.TravelExpenseCreate
        ) -> schema.TravelExpense:
        '''Returns a schema.TravelExpense version of the travel expense.

        :param trip_create: The trip
        :type trip_create: model.TripCreate
        :return: The schema model of the trip
        :rtype: schema.Trip
        '''
        db_travel_expense = schema.TravelExpense(
            expense_id=travel_expense_create.expense_id,
            trip_id=travel_expense_create.trip_id
        )
        return db_travel_expense


    @staticmethod
    def model_travel_expense_to_schmea(
        travel_expense: model.TravelExpense) -> schema.TravelExpense:
        '''Returns a schema.TravelExpense version of the travel expense.

        :param trip_create: The trip
        :type trip_create: model.TravelExpense
        :return: The schema model of the trip
        :rtype: schema.Trip
        '''
        db_travel_expense = schema.TravelExpense(
            _id=travel_expense.travel_expense_id,
            expense_id=travel_expense_create.expense_id,
            trip_id=travel_expense_create.trip_id
        )
        return db_travel_expense
