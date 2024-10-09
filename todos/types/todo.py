from pydantic import BaseModel,Field
from typing import List
from ..models.todo_model import Todo

class Get_Todos_Response(BaseModel):
    detail:str
    todos:List[Todo]

class Todo_Response(BaseModel):
    detail:str
    todo:Todo

class Create_Todo_Request(BaseModel):
    title: str = Field(
        ..., 
        example="Todo title", 
        description="Enter Title"
    )
    description: str = Field(
        ..., 
        example="This is test description",
        description="Enter your Description"
    )
    is_done: bool = Field(
        ..., 
        example=False, 
        description="Is the todo done"
    )
class Update_Todo_Request(BaseModel):
    title: str = Field(
        ..., 
        example="Updated title", 
        description="Enter Title"
    )
    description: str = Field(
        ..., 
        example="This is update description",
        description="Enter your Description"
    )
    is_done: bool = Field(
        ..., 
        example=True, 
        description="Is the todo done"
    )

class Delete_Todo_Response(BaseModel):
        detail:str