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
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# class User(BaseModel):
#     username: str
#     full_name: str | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results

"""
FastAPI will do the automatic conversion from the request, so that the parameter item receives its specific 
content and the same for user.
It will perform the validation of the compound data, and will document it like that for the OpenAPI schema and 
automatic docs.

Singular values in body
"""

# from typing import Annotated
# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# class User(BaseModel):
#     username: str
#     full_name: str | None = None

# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int, item: Item, user: User, importance: Annotated[int, Body()]):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     return results

"""Multiple body params and query """

# from typing import Annotated
# from fastapi import Body, FastAPI
# from pydantic import BaseModel
# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# class User(BaseModel):
#     username: str
#     full_name: str | None = None

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Item,
#     user: User,
#     importance: Annotated[int, Body(gt=0)],
#     q: str | None = None,
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     if q:
#         results.update({"q": q})
#     return results

"""
Embed a single body parameter
Let's say you only have a single item body parameter from a Pydantic model Item.

By default, FastAPI will then expect its body directly.

But if you want it to expect a JSON with a key item and inside of it the model contents, as it does when you
declare extra body parameters, you can use the special Body parameter embed:
"""

# from typing import Annotated

# from fastapi import Body, FastAPI
# from pydantic import BaseModel
# app = FastAPI()
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int|float, item: Annotated[Item, Body(embed=True)]):
#     results = {"item_id": item_id, "item": item}
#     return results