from dataclasses import dataclass
from datetime import date
from skyhelper_backend.domain.enums import UserTypes


@dataclass
class User:
    user_id: int
    
    role: UserTypes
    
    first_name: str
    last_name: str
    patronymic: str | None
    
    birth_date: date


    
    
    