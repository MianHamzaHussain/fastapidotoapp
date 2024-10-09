internal_server_error = {
    "description": "Internal Server Error",
    "content": {
        "application/json": {
            "example": {
                "detail": "Internal Server Error: detailed error message"
            }
        }
    }
}


not_found = {
    "description": "Todo not found",
    "content": {
        "application/json": {
            "example": {
                "detail": "Todo not found"
            }
        }
    }
}

not_authorized = {
    "description": "Not authorized to access this todo",
    "content": {
        "application/json": {
            "example": {
                "detail": "Not authorized to access this todo"
            }
        }
    }
}

# Response for Listing Todos
list_todos_responses = {
    200: {
        "description": "List of todos",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Todos fetched successfully",
                    "todos": [
                        {"id": 1, "title": "Sample Todo", "description": "Sample description", "is_done": False,"owner_id":1}
                    ]
                }
            }
        }
    },
    500: internal_server_error,
}

# Response for Fetching Todo Detail
detail_todo_responses = {
    200: {
        "description": "Todo fetched successfully",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Todo fetched successfully",
                    "todo": {
                        "id": 1,
                        "title": "Sample Todo",
                        "description": "Sample description",
                        "is_done": False,
                        "owner_id":1
                    }
                }
            }
        }
    },
    404: not_found,
    403: not_authorized,
    500: internal_server_error,
}

# Response for Creating Todo
create_todo_responses = {
    201: {
        "description": "Todo created successfully",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Todo created successfully",
                    "todo": {
                        "id": 1,
                        "title": "Sample Todo",
                        "description": "Sample description",
                        "is_done": False,
                        "owner_id":1
                    }
                }
            }
        }
    },
    500: internal_server_error,
}

update_todo_responses = {
    201: {
        "description": "Todo updated successfully",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Todo updated successfully",
                    "todo": {
                        "id": 1,
                        "title": "Sample Todo",
                        "description": "Sample description",
                        "is_done": False,
                        "owner_id":1
                    }
                }
            }
        }
    },
    404: not_found,
    403: not_authorized,
    500: internal_server_error
}

delete_todo_responses = {
    200: {
        "description": "Todo deleted successfully",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Todo deleted successfully",
                }
            }
        }
    },
    404: not_found,
    403: not_authorized,
    500: internal_server_error
}