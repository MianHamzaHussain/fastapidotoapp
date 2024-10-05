from fastapi import FastAPI, Body, HTTPException, Path, Depends
import uvicorn
import os
from typing import Annotated, List
from dotenv import load_dotenv
from .models.todo import Todo
from .config.db import engine, create_tables
from sqlmodel import Session, select

load_dotenv()

app = FastAPI()
@app.get("/",response_model=dict,responses={
    200:{
          "description": "Server running details",
        "content": {
            "application/json": {
                "example":{
                    "message": "Server is running",
  "url": "http://127.0.0.1:8080"
                }
            }
        }

    }
})
def read_root():
    host = os.getenv("HOST", "127.0.0.1")  # Get host from environment variable or default
    port = os.getenv("PORT", "8080")        # Get port from environment variable or default
    url = f"http://{host}:{port}"
    return {"message": "Server is running", "url": url}

def get_session() -> Session:
    return Session(engine)  # Return session without 'with' context

@app.get("/todos", response_model=List[Todo], responses={
    200: {
        "description": "List of todos",
        "content": {
            "application/json": {
                "example": [
                    {"id": 1, "title": "Sample Todo", "description": "sample description", "is_done": False}
                ]
            }
        }
    },
    500: {
        "description": "Internal Server Error",
        "content": {
            "application/json": {
                "example": {"detail": "An error occurred while fetching todos"}
            }
        }
    }
})
def get_todos(session: Annotated[Session, Depends(get_session)]) -> List[Todo]:
    try:
        statement = select(Todo)
        results = session.exec(statement).all()
        return results
    except Exception as e:
        print(f"error in get_todos {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred while fetching todos: {str(e)}")

@app.get("/todos/{id}", response_model=Todo, responses={
    200: {
        "description": "Todo retrieved successfully",
        "content": {
            "application/json": {
                "example": {
                    "id": 1,
                    "title": "Sample Todo",
                    "description": "sample description",
                    "is_done": False
                }
            }
        }
    },
    404: {
        "description": "Todo not found",
        "content": {
            "application/json": {
                "example": {"detail": "Todo with id 1 not found"}
            }
        }
    }
})
def get_detail_todo(
    session: Annotated[Session, Depends(get_session)],
    id: Annotated[int, Path(..., gt=0, description="The ID of the todo to retrieve")], 
) -> Todo:
    try:
        existing_todo = session.get(Todo, id)
        if not existing_todo:
            raise HTTPException(status_code=404, detail=f"Todo with id {id} not found")
        return existing_todo
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while fetching the todo: {str(e)}")

@app.post("/todos", response_model=Todo, responses={
    201: {
        "description": "Todo successfully created",
        "content": {
            "application/json": {
                "example": {
                    "id": 1,
                    "title": "New Task",
                    "description": "New task description",
                    "is_done": False
                }
            }
        }
    },
    500: {
        "description": "Internal Server Error",
        "content": {
            "application/json": {
                "example": {"detail": "An error occurred while creating todos"}
            }
        }
    }
})
def create_todos(
    session: Annotated[Session, Depends(get_session)],
    todo: Todo = Body(
        example={
            "title": "New Task",
            "description": "New task description",
            "is_done": False
        }
    ),
) -> Todo:
    try:
        new_todo = Todo(title=todo.title, description=todo.description, is_done=todo.is_done)
        session.add(new_todo)
        session.commit()
        session.refresh(new_todo)
        return new_todo
    except Exception as e:
        print(f"error in create_todos {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred while creating todos: {str(e)}")

@app.put("/todos/{id}", response_model=Todo, responses={
    200: {
        "description": "Todo successfully updated",
        "content": {
            "application/json": {
                "example": {
                    "id": 1,
                    "title": "Updated Task",
                    "description": "Updated description",
                    "is_done": True
                }
            }
        }
    },
    404: {
        "description": "Todo not found",
        "content": {
            "application/json": {
                "example": {"detail": "Todo with id 1 not found"}
            }
        }
    }
})
def update_todo(
    session: Annotated[Session, Depends(get_session)],
    id: Annotated[int, Path(..., gt=0, description="The ID of the todo to update")],
    todo: Todo = Body(
        example={
            "title": "Updated Title", 
            "description": "Update task description", 
            "is_done": False
        }
    ),
) -> Todo:
    try:
        existing_todo = session.get(Todo, id)
        if not existing_todo:
            raise HTTPException(status_code=404, detail=f"Todo with id {id} not found")
        existing_todo.title = todo.title
        existing_todo.description = todo.description
        existing_todo.is_done = todo.is_done
        session.add(existing_todo)
        session.commit()
        session.refresh(existing_todo)
        return existing_todo
    except Exception as e:
        print(f"error in update_todo {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred while updating the todo: {str(e)}")

@app.delete("/todos/{id}", response_model=dict, responses={
    200: {
        "description": "Todo successfully deleted",
        "content": {
            "application/json": {
                "example": {"message": "Todo successfully deleted"}
            }
        }
    },
    404: {
        "description": "Todo not found",
        "content": {
            "application/json": {
                "example": {"detail": "Todo with id 1 not found"}
            }
        }
    }
})
def delete_todo(id: Annotated[int, Path(..., gt=0, description="The ID of the todo to delete")], session: Annotated[Session, Depends(get_session)]) -> dict:
    try:
        existing_todo = session.get(Todo, id)
        if not existing_todo:
            raise HTTPException(status_code=404, detail=f"Todo with id {id} not found")
        
        session.delete(existing_todo)
        session.commit()
        return {"message": "Todo successfully deleted"}
    except Exception as e:
        print(f"error in delete_todo {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred while deleting the todo: {str(e)}")

def start() -> None:
    create_tables()
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 8000))
    uvicorn.run("todos.main:app", host=host, port=port, reload=True)

