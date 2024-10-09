from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from .auth_model import Auth
class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    is_done: bool = False
    owner_id: Optional[int] = Field(default=None, foreign_key="auth.id")  
    owner: Optional[Auth] = Relationship(back_populates="todos")
