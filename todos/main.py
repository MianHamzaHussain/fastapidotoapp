from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
from .config.db import  create_tables
from .routes import todo_routes ,auth_routes
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
app.include_router(auth_routes.router)
app.include_router(todo_routes.router)

def start() -> None:
    create_tables()
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 8000))
    uvicorn.run("todos.main:app", host=host, port=port, reload=True)

