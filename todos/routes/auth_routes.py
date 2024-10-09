from  fastapi import APIRouter,Depends,HTTPException, Path
from sqlmodel import Session
from ..controllers import auth_controller
from ..models.auth_model import Auth
from ..config.db import get_session
from ..types.auth import SignUpRequest,SignInRequest,SignInResponse,SignUpResponse
from ..example_responses.auth_example import signup_responses,signin_responses
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter()

@router.post('/auth/signup',response_model=SignUpResponse,responses=signup_responses)
def signup(data: SignUpRequest, session: Session = Depends(get_session)):
      return auth_controller.signup(data,session)


@router.post('/auth/signin', response_model=SignInResponse, responses=signin_responses)
def signin(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    data = SignInRequest(user_name_or_email=form_data.username, password=form_data.password)
    return auth_controller.signin(data, session)