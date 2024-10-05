from sqlmodel import Field, SQLModel

class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    is_done:bool=False