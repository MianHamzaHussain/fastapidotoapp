from sqlmodel import Session,select
from ..models.todo_model import Todo
from ..models.auth_model import Auth
from fastapi import HTTPException

def get_all_todos(current_user: Auth, session: Session):
    try:
        todos = session.query(Todo).filter(Todo.owner_id == current_user.id).all()
        
        # Returning a structured response
        return {
            "detail": "Todos fetched successfully",
            "todos": todos
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


def get_todo_by_id(todo_id: int, current_user: Auth, session: Session):
    try:
        todo = session.get(Todo, todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        if todo.owner_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized to access this todo")
        return {
            "detail":"Todo fetched successfully",
            "todo":todo,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

def create_todo(todo_request: Todo,current_user: Auth, session: Session):
    try:
        todo = Todo(
            title=todo_request.title,
            description=todo_request.description,
            is_done=todo_request.is_done
        )
        todo.owner_id = current_user.id
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return {
            "detail":"Todo created successfully",
            "todo":todo,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
def update_todo(todo_id: int, updated_todo: Todo, current_user: Auth, session: Session):
    try:
        todo = session.get(Todo, todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        if todo.owner_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized to update this todo")
        
        todo.title = updated_todo.title
        todo.description = updated_todo.description
        todo.is_done = updated_todo.is_done
        session.commit()
        session.refresh(todo)
        return {
            "detail": "Todo updated successfully",
            "todo": todo,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


def delete_todo(todo_id: int, current_user: Auth, session: Session):
    try:
        todo = session.get(Todo, todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        if todo.owner_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not authorized to delete this todo")
        
        session.delete(todo)
        session.commit()
        return {"detail": "Todo successfully deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
