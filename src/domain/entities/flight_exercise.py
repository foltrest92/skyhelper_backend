
from datetime import datetime

from . import Minimum


class FlightsExercise:
    flights_exercise_id: int
    
    aircraft_id: int
    pilot_id: int
    
    short_description: str | None
    
    crew_exercises: dict[tuple[object, dict[object]]] | None #TODO: Состав экипажа с упражнениями
    
    examinator_id: int | None
    departure_datetime: datetime
    arrived_datetime: datetime
    
    routes: str
    places: dict[str]
    
    minimum: Minimum
    
    
    