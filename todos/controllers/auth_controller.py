from sqlmodel import Session,select
from ..models.auth_model import Auth
from fastapi import HTTPException
from datetime import timedelta
from ..types.auth import SignUpRequest,SignInRequest
from ..share.utility import get_password_hash,verify_password,create_access_token

def signup(data:SignUpRequest, session: Session):
    try:
        existing_user_name= session.exec(
        select(Auth).where(Auth.user_name == data.user_name)
        ).first()
        existing_email = session.exec(
        select(Auth).where(Auth.email == data.email)
        ).first()

        if existing_user_name:
            raise HTTPException(status_code=400, detail="Username already exists")
    
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already exists")
        new_user = Auth(
        user_name=data.user_name,
        email=data.email,
        password=get_password_hash(data.password)  # Hash the password
        )

    # Add the new user to the session and commit
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return {
            "detail": "User signup successfully",
            "user": {
            "id": new_user.id,
            "user_name": new_user.user_name,
            "email": new_user.email
            }
  
           
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(error)}")


def signin(data: SignInRequest, session: Session):
    try:
        user = session.exec(
            select(Auth).where(
                (Auth.user_name == data.user_name_or_email) | (Auth.email == data.user_name_or_email)
            )
        ).first()

        if not user or not verify_password(data.password, user.password):
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token = create_access_token(data={"sub": user.user_name}, expires_delta=timedelta(minutes=30))
        print(f"Access Token: {access_token}")
        # Return response
        return {"detail": "User logged in successfully", "access_token": access_token}

    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Internal Server Error:{str(error)}")
