from skyhelper_backend.domain.entities import Minimum
from skyhelper_backend.domain.entities import User


class Instructor(User):
    minimum: Minimum | None