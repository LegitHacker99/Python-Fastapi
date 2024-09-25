from datetime import datetime
from uuid import UUID
from fastapi import FastAPI, File, Form, HTTPException, Query, Path, Body, UploadFile
from enum import Enum
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from typing import Any

from routers.chats import router as chats_router
from routers.users import router as users_router

app = FastAPI(swagger_ui_parameters={
    "tryItOutEnabled": True,
    "requestSnippetsEnabled": True,
})

app.include_router(chats_router)
app.include_router(users_router)

class Image(BaseModel):
    url: HttpUrl = Field(..., example='https://www.google.com')
    name: str = Field(..., example='Google')

class Item(BaseModel):
    price: int = Field(..., example=20)
    name: str = Field(..., example='Item_name')
    date: datetime | None = None
    desc: str | None = Field(None, example='Description Of Item')
    tax: int | None = Field(None, example=1075)
    image: list[Image] | None = None

class User(BaseModel):
    username: str
    password: str
    email: EmailStr = Field(...)
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr = Field(...)
    full_name: str | None = None

fake_db_2 = {}

# @app.post('/user', tags=["user"], response_model=UserOut) # using a response_model allows fastapi to filter the returned object as per the object type described in the response_model param w/o manual serialization
# def login(user: User) -> Any:
#     return user


# class FoodEnum(str, Enum):
#     vegetable = "vegetables"
#     fruits = "fruits"
#     dairy = "dairy"

# fake_items_db = [{"item": "foo"}, {"item": "bar"}, {"item": "baz"}, {"item": "jazz"}, {"item": "sass"}]

# @app.get('/', description='Index Route', tags=['Index'])
# def helloworld():
#     return {"msg": "Hello Word;"}

# '''
#     Can not name query param & route method name the same
# '''

# @app.get('/users', tags=['Users'])
# def list_users():
#     '''
#     - **name** : demo docstring in fastapi
#     '''
#     return {"users": "users_list"}

# # should be before to allow matching of routes, just how fastapi works
# @app.get('/users/me')
# def get_current_user():
#     return {"user_id": "This is me"}

# @app.get('/users/{user_id}')
# def get_user(user_id: int):
#     return {"user_id": user_id}

# @app.get('foods/{food_name}')
# def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.dairy:
#         return {"food_name": food_name, "msg": "healthy"}
    
#     if food_name == FoodEnum.fruits:
#         return {"food_name": food_name, "msg": "medium healthy"}
    
#     return {"food_name": food_name, "msg": "low heaalthy"}

# @app.get('/list_items')
# def list_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip:limit]

# @app.get('/list_items/{item_id}')
# def list_items(item_id: int = Path(...), q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"descr": "अङ्गेन गात्रं नयनेन वक्त्रं न्यायेन राज्यं लवणेन भोज्यं"})
    
#     return item


# @app.post('/post_item')
# def post_func(item: Item, q: list[str] | str = Query(..., max_length=10, min_length=1, alias='item-query')):
#     # here, `...` allows us to make the query param a req one as well as not provide a default value
#     # also escape char like `-` using alias for query param
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
    
#     if q:
#         item_dict.update({"q": q})

#     return item_dict

# @app.get('/hidden_query_param')
# def hidden_query_param_route(*, hidden: str | None = Query(None, include_in_schema=False), next_param: str):
#     # adding * as the first param allows to convert all the params as keyword params as python does not allows non-default args to be declared after default args
#     if hidden:
#         return {
#             "msg": hidden,
#             "nest_param": next_param
#         }
    
#     return {
#         "msg": 'No hidden Params',
#         "nest_param": next_param
#     }

# class User(BaseModel):
#     id: int = Field(..., json_schema_extra={"key": "value"}, gt=9)
#     full_name: str

# @app.post('/multiple_body_param/{item_id}')
# def handle_multiple_body_param(*, item_id: int, q: str | None = None, item: Item = Body(...), user: User | None):
#     response = {}
#     response.update({"item_id": item_id})
#     if q:
#         response.update({"q": q})
    
#     if item:
#         response.update({"item": item})

#     if user:
#         response.update({"User": user})
    
#     return response


# @app.post('/uplad_logo')
# def upload_logo(itme: Item, blah: dict[int, float] = Body(..., example={"1": 45.05, "2": 3})):
#     return {"logo_details": itme, "blah_details": blah}

# @app.put('check_other_dtypes')
# def check_other_dtypes(item_uuid: UUID, created_at: datetime = Body(...), end_at: datetime = Body(...)):
#     resp = {}
#     duration = end_at - created_at
#     resp.update({"item_uuid": item_uuid, "duration": duration})
#     return resp


# @app.post('/login')
# def login(username: str = Form(...), password: str = Form(...)):
#     print(password)
#     return {"username": username}

# @app.post('/file')
# def file(files: list[bytes] | None = File(None)):
#     '''
#         Un-tested endpoint
#     '''
#     if not files:
#         return {"msg": "No files found"}
    
#     return {"file_len": [len(file) for file in files]}

# @app.post('upload_file')
# def upload_files(files: list[UploadFile] = File(...)):
#     '''
#         Un-tested endpoint, please test this
#     '''
#     return {"file_name": [file.filename for file in files]}

# items = {
#     "foo": "the foo wrestlers"
# }


# @app.put('/foo_path/{item_id}', tags=["foo_path"])
# def foo_wrestlers(item_id: str, item: Item):
#     # if item_id not in items:
#     #     raise HTTPException(status_code=404, detail="Item not found")
    
#     json_compatible_data = jsonable_encoder(item)
#     fake_db_2[item_id] = item
#     print(fake_db_2)
#     return fake_db_2
