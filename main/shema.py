from typing import Optional
from pydantic import BaseModel, EmailStr, validator

@validator('books', pre=True, allow_reuse=True)
def pony_set_to_list(cls, values):
    new_values = list()
    for v in values:
        if hasattr(v, "to_dict"):
            new_values.append(v.to_dict())
    return new_values


class Config:
    orm_mode = True

class Return_all_books(BaseModel):
    id: int
    page_count: int
    name: str
    prise: float
    author: str



  #  @validator('author', pre=True, allow_reuse=True)
  #  def pony_set_to_list(cls, value):
  #      if hasattr(value, "to_dict"):
  #          value = value.to_dict()
  #      return value

  #  class Config:
  #      orm_mode = True