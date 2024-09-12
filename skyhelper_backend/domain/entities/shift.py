from dataclasses import dataclass
from datetime import date, datetime
from skyhelper_backend.domain.entities import User, ShiftItem


@dataclass
class Shift:
    shift_id: int

    shift_date: date | None
    shift_start: datetime | None
    shift_end: datetime | None

    senior: User | None
    approved_by: User | None
    approved_date: date | None

    shift_items: dict[ShiftItem]

    results: str | None
    remarks: str | None
    instructions: str | None