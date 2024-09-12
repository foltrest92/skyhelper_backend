from dataclasses import dataclass
from datetime import time


@dataclass
class ExerciseMeteo:
    exercise_meteo_id: int
    
    place: str

    alt: int
    wind_velocity: int
    wind_direction: int

    sunrise_time: time
    rising_time: time
    sunset_time: time
    dark_time: time

    visibility: int
    ceiling: int
    temp: int
    qfe: int
    qnh: int
