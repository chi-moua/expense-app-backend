from app.database.connection import DBConnectionManager
from app.database.model.schema import Trip


class TripDao:
    '''The Trip Dao contains CRUD functionality that interacts with the database.'''

    def __init__(self):
        self.db = DBConnectionManager.get_db()

    
    @classmethod
    def get_dao(cls):
        '''Gets an instance of the trip Dao.

        :return: The trip Dao
        :rtype: tripDao
        '''
        return cls()


    def create_trip(trip: Trip):
        '''Adds the trip to the database.

        :param trip: The trip
        :type trip: database.model.schema.Trip
        :return: The trip
        :rtype: database.model.schema.Trip
        '''
        self.db.add(trip)
        self.db.commit()
        return trip


    def get_trip_by_id(trip_id: int):
        '''Gets the trip with the given id.

        :param trip_id: The trip id.
        :type trip_id: Integer
        :return: The trip
        :rtype: database.model.schema.Trip
        '''
        return self.db.query(trip).get(trip_id)


    def get_all_trips():
        '''Gets all the trips.

        :return: The trips
        :rtype: List[database.model.schema.Trip]
        '''
        return self.db.query(trip).all()


    def update_trip(trip: trip):
        '''Updates the given trip to the database.
        
        :param trip: The trip
        :param updates: The updates
        :type trip: database.model.schema.trip
        :type updates: Dictionary
        :return: The trip
        :rtype: database.model.schema.trip
        '''
        self.db.commit()
        return trip
    

    def delete_trip(trip: trip):
        '''Deletes the given trip in the database.

        :param trip: The trip
        :type trip: database.model.schema.trip
        '''
        self.db.delete(trip)
        self.db.commit()