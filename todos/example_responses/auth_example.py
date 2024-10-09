internal_server_error={
        "description": "Internal Server Error",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Internal Server Error: detailed error message"
                }
            }
        }
    }
signup_responses= {200: {
        "description": "User successfully created",
        "content": {
            "application/json": {
                "example": {
                    "detail": "User created successfully",
                    "user": {
                        "username": "new_user",
                        "email": "new_user@example.com",
                        "id":1
                    }
                }
            }
        }
    },
    400: {
        "description": "User name or password is incorrect",
        "content": {
            "application/json": {
                "example": {
                    "detail": "User name or password is incorrect"
                }
            }
        }
    },
    500:internal_server_error,
   
}


signin_responses= {200: {
        "description": "User logged in successfully",
        "content": {
            "application/json": {
                "example": {
                    "detail": "User logged in successfully",
                     "access_token":"token string"
                }
            }
        }
    },
    400: {
        "description": "Username or Email already exists",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Username already exists"
                }
            }
        }
    },
    500:internal_server_error
}