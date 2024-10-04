from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from app.deps import get_user_token
from typing import Any

router = APIRouter(
    prefix='/users',
    tags=["users"],
    responses={404: {"description": "Not Found"}},
    dependencies=[Depends(get_user_token)]
)

class User(BaseModel):
    id: int
    username: str
    fullname: str

user1 = User(id=0, username="davidputra", fullname='Indian bison')
user2 = User(id=1, username="Deadpond", fullname='Dive Wilson')
user3 = User(id=2, username="trans-Spider", fullname='Pedro Parqueador')
user4 = User(id=3, username="Rusty-Man", fullname='Tommy Sharp')

users_db = []

@router.get("/")
def get_all_users() -> list[User]:
    global users_db
    if not users_db:
        users_db = [user1, user2, user3, user4]
        
    return users_db

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_users(user: User) -> int:
    global users_db
    if user:
        users_db.append(user)

    return user.id

@router.delete("/{user_id}", status_code=status.HTTP_202_ACCEPTED)
def delete_account(user_id: int) -> Any:
    global users_db
    for i in range(len(users_db)):
        if users_db[i].id == user_id:
            users_db.pop(i)
        
        # db.commit()  ## some action to persist the change

    return f'Chat with id {user_id} deleted'




