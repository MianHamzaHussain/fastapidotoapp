from pydantic import BaseModel, Field, validator
import re

class SignUpRequest(BaseModel):
    user_name: str = Field(
        ..., 
        min_length=3, 
        max_length=50, 
        example="john_doe", 
        description="Username must be between 3 and 50 characters."
    )
    email: str = Field(
        ..., 
        example="john.doe@example.com",
        description="Must be a valid email address."
    )
    password: str = Field(
        ..., 
        min_length=8, 
        max_length=13,
        example="Password@123", 
        description=(
            "Password must be between 8 and 13 characters long, "
            "and contain at least one uppercase letter, one lowercase letter, one digit, "
            "one special character from [@$!%*#?&], and no restricted characters (' , \" , & , + , ? , < , >)."
        )
    )
    @validator('email')
    def validate_email(cls, value):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, value):
            raise ValueError('Email is invalid')
        return value
    @validator('password')
    def password_complexity(cls, value):
        if len(value) < 8 or len(value) > 13:
            raise ValueError('Password length must be between 8 and 13 characters.')
        if not re.search(r'[a-z]', value):
            raise ValueError('Password must contain at least one lowercase letter.')
        if not re.search(r'[A-Z]', value):
            raise ValueError('Password must contain at least one uppercase letter.')
        if not re.search(r'\d', value):
            raise ValueError('Password must contain at least one numeric character.')
        if not re.search(r'[@$!%*#?&]', value):
            raise ValueError('Password must contain at least one special character from [@$!%*#?&].')
        
        if re.search(r"[\'\"&+?<>]", value):
            raise ValueError('Password must not contain the following characters: \' " & + ? < >')
        
        return value
class UserResponse(BaseModel):
    id: int
    user_name: str
    email: str

class SignUpResponse(BaseModel):
    detail: str
    user: UserResponse
    
class SignInRequest(BaseModel):
    user_name_or_email:str=Field(
        ..., 
        example="john_doe or john@example.com", 
        description="Enter user name or email"
    )
    password:str=Field(
        ..., 
     example="Password@123",
     description="Enter your password"
    )

class SignInResponse(BaseModel):
    detail: str
    access_token: str