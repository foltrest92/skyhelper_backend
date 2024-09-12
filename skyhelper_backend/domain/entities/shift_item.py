from dataclasses import dataclass
from datetime import timedelta
from skyhelper_backend.domain.entities import User, Aircraft


@dataclass
class ShiftItem:
    shift_item_id: int

    instructor: User
    aircraft: Aircraft
    students_num: int

    flighttime_planned_edu: timedelta
    flights_planned_edu: int
    flighttime_planned_commander: timedelta
    flights_planned_commander: int

    flighttime_real_edu: timedelta
    flights_real_edu: int
    flighttime_planned_commander: timedelta
    flights_planned_commander: int