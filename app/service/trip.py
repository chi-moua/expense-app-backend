from typing import List

from app.database.dao.trip import TripDao
from app.router.model import model
from app.database.model import schema
from app.util.transform import ModelTransformManager


class TripService:
    '''The Trip Service contains the business logic layer for the Trip related data.'''

    def __init__(self):
        self.tripDao = TripDao.get_dao()


    @classmethod
    def get_service(cls):
        '''Gets an instance of the Trip Service.

        :return: The Trip Service
        :rtype: TripService
        '''
        return cls()


    def create_trip(self, trip: model.TripCreate):
        '''Adds the trip to the database.

        :param trip: The trip
        :type trip: router.model.model.TripCreate
        :return: The trip
        :rtype: database.model.schema.Trip
        '''
        db_trip = ModelTransformManager \
            .model_trip_create_to_schema(trip)
        db_trip = self.tripDao.create_trip(db_trip)
        return db_trip


    def get_trip_by_id(self, trip_id: int):
        '''Gets the trip with the given id.

        :param trip_id: The trip id.
        :type trip_id: Integer
        :return: The trip
        :rtype: database.model.schema.Trip
        '''
        #TODO: handle trip not found
        db_trip = self.tripDao.get_trip_by_id(trip_id):
        if not db_trip:
            pass
        return db_trip

    
    def get_all_trips(self):
        '''Gets all the trips.

        :return: The trips
        :rtype: List[database.model.schema.Trip]
        '''
        return self.tripDao.get_all_trips():


    def update_trip(self, trip: model.Trip):
        '''Updates the given trip to the database.
        
        :param trip: The trip
        :type trip: router.model.model.Trip
        :return: The trip
        :rtype: database.model.schema.trip
        '''
        db_trip = ModelTransformManager \
            .model_trip_to_schema(trip)
        db_trip = self.tripDao.update_trip(db_trip)
        return db_trip


    def delete_trip(self, trip: model.Trip):
        '''Deletes the given trip in the database.

        :param trip: The trip
        :type trip: router.model.model.Trip
        '''
        db_trip = ModelTransformManager \
            .model_trip_to_schema(trip)
        db_trip = self.tripDao.delete_trip(db_trip)
        return
