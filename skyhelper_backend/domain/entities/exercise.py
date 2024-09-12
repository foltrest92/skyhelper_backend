from datetime import timedelta
from skyhelper_backend.domain.enums import ExerciseTypes


class Exercise:
    exercise_id: int
    exercise_name: str

    exercise_module: int
    exercise_type: ExerciseTypes
    exercise_num: int

    is_night: bool = False

    next_exercise: dict
    prev_exercise: dict

    flight_time: timedelta
    flight_time_ifr: timedelta

    landings: int
    approaches: int


    def __init__(
            self,
            exercise_id: int,
            exercise_name: str,
            exercise_module: int,
            exercise_type: ExerciseTypes,
            exercise_num: int,
            next_exercise: dict,
            prev_exercise: dict,
            flight_time: timedelta,
            flight_time_ifr: timedelta,
            landings: int,
            approaches :int,
            is_night: bool = False
    ):
        self.exercise_id = exercise_id
        self.exercise_name = exercise_name
        self.exercise_module = exercise_module
        self.exercise_type = exercise_type
        self.exercise_num = exercise_num
        self.next_exercise =  next_exercise
        self.prev_exercise = prev_exercise
        self.flight_time = flight_time
        self.flight_time_ifr = flight_time_ifr
        self.landings = landings
        self.approaches = approaches
        self.is_night = is_night
        


