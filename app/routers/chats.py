from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, Field
from app.deps import get_user_token
from typing import Any

router = APIRouter(
    prefix='/chats',
    tags=["chats"],
    responses={404: {"description": "Not Found"}},
    dependencies=[Depends(get_user_token)]
)

class Chat(BaseModel):
    id: int
    members: list[int]

chat1 = Chat(id=0, members=[0, 1])
chat2 = Chat(id=1, members=[1, 2])
chats_db = [chat1, chat2]

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_all_chats(user_id: int) -> list[Chat] | str:
    global chats_db
    resp_obj = []
    # if user_id in chat1.members and user_id in chat2.members:
    #     resp_obj.append(chat1)
    #     resp_obj.append(chat2)
    #     return resp_obj
    
    # for chat in [chat1, chat2]:
    #     if user_id in chat.members:
    #         resp_obj.append(chat)
    for chat in chats_db:
        if user_id in chat.members:
            resp_obj.append(chat)

    if resp_obj is not None:
        return resp_obj
    
    return f'No chats for {user_id}'


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_users(chat: Chat) -> int:
    global chats_db
    if chat:
        chats_db.append(chat)

    return chat.id


@router.delete("/{chat_id}", status_code=status.HTTP_202_ACCEPTED)
def delete_chat(chat_id: int) -> Any:
    global chats_db
    for i in range(len(chats_db)):
        if chats_db[i].id == chat_id:
            chats_db.pop(i)
        # db.commit()  ## some action to persist the change

    return f'Chat with id {chat_id} deleted'

