from datetime import datetime

from skyhelper_backend.domain.entities import Exercise
from skyhelper_backend.domain.entities import User

from . import Minimum


class FlightsExercise:
    flights_exercise_id: int
    
    aircraft_id: int
    pilot_id: int
    
    short_description: str | None
    
    crew_exercises: dict[tuple[User, dict[Exercise]]] | None
    
    examinator_id: int | None
    departure_datetime: datetime
    arrived_datetime: datetime
    
    routes: str
    places: dict[str]
    
    minimum: Minimum
    
    
    