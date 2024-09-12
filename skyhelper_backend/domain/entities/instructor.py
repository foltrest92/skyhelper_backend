from dataclasses import dataclass
from skyhelper_backend.domain.entities import Minimum, User


@dataclass
class Instructor(User):
    minimum: Minimum | None