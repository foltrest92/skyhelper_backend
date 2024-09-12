from dataclasses import dataclass
from skyhelper_backend.domain.entities import User


@dataclass
class Student(User):
    group_id: int