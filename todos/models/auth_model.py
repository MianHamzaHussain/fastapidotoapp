from sqlmodel import Field, SQLModel, Relationship
from typing import List

class Auth(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_name: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    password: str
    todos: List["Todo"] = Relationship(back_populates="owner")
