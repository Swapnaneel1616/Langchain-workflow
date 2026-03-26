from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Person(BaseModel):
    name: str = 'Neel'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10 , default=5)
new_person = {"age": 23, "email": "neel@gmail.com", "cgpa": 9.5}

person = Person(**new_person)

print(person)

