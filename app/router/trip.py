from fastapi import APIRouter

from app.service.trip import TripService
from app.router.model.model import TripCreate, Trip


router = APIRouter()


@router.post('/trip', tags=['trip'])
def create_trip(trip: TripCreate):
    res_trip = TripService.get_service().create_trip(trip)
    return res_trip


@router.get('/trip/{trip_id}', tags=['trip'])
def get_trip_by_id(trip_id: int):
    res_trip = TripService.get_service().get_trip_by_id(trip_id)
    return res_trip


@router.get('/trip', tags=['trip'])
def get_trip():
    all_trips = TripService.get_service().get_all_trips()
    return all_trips


@router.put('/trip', tags=['trip'])
def update_trip(trip: Trip):
    TripService.get_service().update_trip(trip)
    return


@router.delete('/trip/{trip_id}', tags=['trip'])
def delete_trip(trip_id: int):
    TripService.get_service().delete_trip_by_id(trip_id)
    return