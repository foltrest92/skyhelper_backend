from datetime import datetime, timedelta

from skyhelper_backend.domain.entities import Exercise
from skyhelper_backend.domain.entities import User

class Flight:
    flight_id: int
    
    aircraft_id: int
    
    pilot: User
    copilot: User | None
    third: User | None
    
    provider: User | None
    crew_member: User | None
    
    landings_num: int
    approaches_num: int
    
    exercise: Exercise | None
    
    mark: int | None
    
    place_from: str
    place_to: str | None
    
    start_datetime: datetime
    taxi_start_datetime: datetime
    taxi_stop_datetime: datetime
    stop_datetime: datetime
    
    ground_time: timedelta
    ground_time_night: timedelta | None
    flight_time: timedelta
    flight_time_night: timedelta | None
    flight_time_ifr: timedelta | None
    
    fuel_remaining: int | None
    fuel_fuelled: int | None
    fuel_sum: int | None
    
    garmin_before: float | None
    garmin_flight: float | None
    garmin_after: float | None
    
    comments: str | None
    result: str | None
    
    def __init__(
        self,
        flight_id: int,
        aircraft_id: int,
        pilot: User,
        landings_num: int,
        approaches_num: int,
        place_from: str,
        start_datetime: datetime,
        taxi_start_datetime: datetime,
        taxi_stop_datetime: datetime,
        stop_datetime: datetime,
        ground_time: timedelta,
        flight_time: int,
        copilot: User | None = None,
        third: User | None = None,
        provider: User | None = None,
        crew_member: User | None = None,
        exercise: Exercise | None = None,
        mark: int | None = None,
        place_to: str | None = None,
        ground_time_night: int | None = None,
        flight_time_night: int | None = None,
        flight_time_ifr: int | None = None,
        fuel_remaining: int | None = None,
        fuel_fuelled: int | None = None,
        fuel_sum: int | None = None,
        garmin_before: float | None = None,
        garmin_flight: float | None = None,
        garmin_after: float | None = None,
        comments: str | None = None,
        result: str | None = None
    ):
        self.flight_id = flight_id
        
        self.aircraft_id = aircraft_id
        
        self.pilot = pilot
        self.copilot = copilot
        self.third = third
        
        self.provider = provider
        self.crew_member = crew_member
        
        self.landings_num = landings_num
        self.approaches_num = approaches_num
        
        self.exercise = exercise
        
        self.mark = mark
        
        self.place_from = place_from
        self.place_to = place_to if place_to else place_from
        
        self.start_datetime = start_datetime
        self.taxi_start_datetime = taxi_start_datetime
        self.taxi_stop_datetime = taxi_stop_datetime
        self.stop_datetime = stop_datetime
        
        self.ground_time = ground_time if ground_time else taxi_start_datetime - start_datetime + stop_datetime - taxi_stop_datetime
        self.ground_time_night = ground_time_night # TODO: Учитывать ночь
        
        self.flight_time = flight_time if flight_id else taxi_stop_datetime - taxi_start_datetime
        self.flight_time_night = flight_time_night # TODO: Учитывать ночь
        self.flight_time_ifr = flight_time_ifr # TODO: Учитывать IFR
        
        self.fuel_remaining = fuel_remaining
        self.fuel_fuelled = fuel_fuelled
        if fuel_remaining and fuel_fuelled and not fuel_sum:
            self.fuel_sum = fuel_remaining + fuel_fuelled
        else:
            self.fuel_sum = fuel_sum
        
        self.garmin_before = garmin_before
        self.garmin_after = garmin_after
        if garmin_after and garmin_before and not garmin_flight:
            self.garmin_flight = garmin_after - garmin_before
        else:
            self.garmin_flight = garmin_flight
        
        self.comments = comments
        self.result = result
        