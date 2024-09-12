from dataclasses import dataclass
from datetime import date, datetime
from skyhelper_backend.domain.entities import User, Aircraft, ExerciseMeteo, FlightExerciseReport, Minimum, CrewExercise


@dataclass
class FlightsExercise:
    flights_exercise_id: int
    
    aircraft: Aircraft
    pilot: User
    
    short_description: str | None
    
    crew_exercises: dict[CrewExercise] | None
    
    examinator: Aircraft | None
    departure_datetime: datetime | None
    arrived_datetime: datetime | None
    
    routes: str 
    places: dict[str]
    
    minimum: Minimum

    commander: User | None

    approved_by: User | None
    aprroved_date: date | None

    medical_datetime: datetime | None
    meteo_datetime: datetime | None

    meteo: dict[ExerciseMeteo] | None

    weight: int | None
    center_weight: float | None
    run_up: int | None
    takeoff_distance: int | None
    roll: int | None
    landing_distance: int | None

    preflight_prep: str | None
    notes: str | None

    flight_exercise_report: FlightExerciseReport | None
    
    
    