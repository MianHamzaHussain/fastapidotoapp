from sqlmodel import SQLModel, create_engine
import os
from sqlalchemy.engine import Engine
from typing import Optional

def get_engine() -> Optional[Engine]:
    try:
        db_uri: Optional[str] = os.getenv("DATABASE_URL")
        if db_uri:
            engine = create_engine(db_uri, echo=True)
            print("Successfully connected to the database.")
            return engine
        else:
            raise ValueError("DATABASE_URL environment variable is not set.") 
    except Exception as e:
        print(f"get_engine Error: {e}")
    return None

engine: Optional[Engine] = get_engine()

def create_tables() -> None:
    try:
        if engine:
            SQLModel.metadata.create_all(engine)
            print("Tables created successfully.")
    except Exception as e:
        print(f"create_tables Error: {e}") 
