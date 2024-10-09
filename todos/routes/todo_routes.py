from fastapi import APIRouter, Depends, HTTPException, Path
from sqlmodel import Session
from typing import List
from ..controllers import todo_controller
from ..models.todo_model import Todo
from ..config.db import get_session
from ..example_responses.todo_example import list_todos_responses,detail_todo_responses,create_todo_responses,update_todo_responses,delete_todo_responses
from ..share.utility import get_current_user
from ..models.auth_model import Auth
from ..types.todo import Get_Todos_Response,Todo_Response,Create_Todo_Request,Update_Todo_Request,Delete_Todo_Response
router = APIRouter()

@router.get("/todos", response_model=Get_Todos_Response,responses=list_todos_responses)
def get_todos(current_user: Auth = Depends(get_current_user),session: Session = Depends(get_session)):
    return todo_controller.get_all_todos(current_user,session)

@router.get("/todos/{id}", response_model=Todo_Response,responses=detail_todo_responses)
def get_todo(id: int, current_user:Auth=Depends(get_current_user), session: Session = Depends(get_session)):
    return todo_controller.get_todo_by_id(id,current_user, session)

@router.post("/todos", response_model=Todo_Response,status_code=201,responses=create_todo_responses)
def create_todo(todo:Create_Todo_Request, current_user:Auth=Depends(get_current_user), session: Session = Depends(get_session)):
    return todo_controller.create_todo(todo,current_user, session)

@router.put("/todos/{id}", response_model=Todo_Response,status_code=201,responses=update_todo_responses)
def update_todo(id: int, todo:Update_Todo_Request,current_user:Auth=Depends(get_current_user), session: Session = Depends(get_session)):
    return todo_controller.update_todo(id, todo,current_user, session)

@router.delete("/todos/{id}",response_model=Delete_Todo_Response,responses=delete_todo_responses)
def delete_todo(id: int,current_user:Auth=Depends(get_current_user), session: Session = Depends(get_session)):
    return todo_controller.delete_todo(id,current_user, session)
