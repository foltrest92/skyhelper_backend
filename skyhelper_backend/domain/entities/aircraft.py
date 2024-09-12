from dataclasses import dataclass


@dataclass
class Aircraft:
    aircraft_id: int

    callsign: str

    weight_empty: float
    max_takeoff_weight: float
    bag: float | None
    center_weight: float

    comment: str | None