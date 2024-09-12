from dataclasses import dataclass
from datetime import timedelta
from skyhelper_backend.domain.entities import User


@dataclass
class CrewMembersFlightTime:
    crew_members_flight_time_id: int

    crew_member: User
    flight_time_day: timedelta | None
    flight_time_night: timedelta | None
    flight_time: timedelta
    provided_time: timedelta | None
