"""
Now that we have seen how to use Path and Query, let's see more advanced uses of request body declarations.
"""

# from fastapi import FastAPI, Path
# from typing_extensions import Annotated
# from pydantic import BaseModel

# app =FastAPI()

# class Item(BaseModel):
#     name:str
#     description: str | None = None
#     price: float 
#     tax : float|None = None

# @app.put('/items/{item_id}')
# async def update_item(item_id: Annotated[int, Path(title = "The ID of the item to get", ge = 0, le= 1000)],
#                     q:str|None = None,
#                     item:Item|None = None):
#     results = {'item_id': item_id}
#     if q: 
#         results.update({'q': q})
#     if item:
#         results.update({"item": item})
#     return results

"""
But you can also declare multiple body parameters, e.g. item and user:

"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results
