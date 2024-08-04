from datetime import date
from domain.entities.minimum import Minimum
from domain.enums.user_types import UserTypes


class User:
    user_id: int
    
    role: UserTypes
    
    first_name: str
    last_name: str
    patronymic: str | None
    
    birth_date: date
    minimum: Minimum | None
    
    group_id: int
    
    
    