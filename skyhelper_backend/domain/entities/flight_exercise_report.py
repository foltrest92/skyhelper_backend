from dataclasses import dataclass
from datetime import date, datetime, timedelta
from skyhelper_backend.domain.entities import Aircraft, User, Flight, CrewMembersFlightTime


@dataclass
class FlightExerciseReport:
    flight_exercise_report_id: int

    exercise_id: int

    commander: User
    flight_date: date
    aircraft: Aircraft

    fuel_before: float
    fuelling_before: float
    fuel_before_all: float
    garmin_before: float

    fuel_after: float
    fuelling_after: float
    fuel_after_all: float
    garmin_after: float
    garmin_all: float

    flights: dict[Flight]

    used_fuel: float
    used_deice: float
    user_garmin: float
    fuelling_id: int

    flight_time_day: timedelta
    flight_time_night: timedelta
    flight_time: timedelta

    shift_start: datetime
    shift_end: datetime
    shift_endurance: timedelta

    is_completed: bool
    not_completed_reason: str

    crew_members_flight_times: dict[CrewMembersFlightTime]

    approving_commander: User