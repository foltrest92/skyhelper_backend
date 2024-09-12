from dataclasses import dataclass
from datetime import timedelta
from skyhelper_backend.domain.enums import ExerciseTypes


@dataclass
class Exercise:
    exercise_id: int
    exercise_name: str

    exercise_module: int
    exercise_type: ExerciseTypes
    exercise_num: int


    next_exercises: dict | None
    prev_exercises: dict | None

    flight_time: timedelta
    flight_time_ifr: timedelta

    landings: int
    approaches: int

    is_night: bool = False

