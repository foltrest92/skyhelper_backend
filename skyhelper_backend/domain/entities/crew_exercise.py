from dataclasses import dataclass
from skyhelper_backend.domain.entities import User, Exercise


@dataclass
class CrewExercise:
    crew_exercise_id: int
    
    pilot: User
    exercises: Exercise
    is_second: bool = False