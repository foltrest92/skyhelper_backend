from dataclasses import dataclass
from datetime import datetime, timedelta
from skyhelper_backend.domain.entities import Exercise, User, Aircraft


@dataclass
class Flight:
    flight_id: int
    
    aircraft: Aircraft
    
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
    
    fuel_remaining: float | None
    fuel_fuelled: float | None
    fuel_sum: float | None
    
    garmin_before: float | None
    garmin_flight: float | None
    garmin_after: float | None
    
    comments: str | None
    result: str | None
        