
"""
When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.
A request body is data sent by the client to your API. A response body is the data your API sends to the client.
Your API almost always has to send a response body. But clients don't necessarily need to send request bodies all the 
time, sometimes they only request a path, maybe with some query parameters, but don't send a body.
To declare a request body, you use Pydantic models with all their power and benefits.

To send data, you should use one of: POST (the more common), PUT, DELETE or PATCH.
Sending a body with a GET request has an undefined behavior in the specifications, nevertheless, it is supported by 
FastAPI, only for very complex/extreme use cases.
As it is discouraged, the interactive docs with Swagger UI won't show the documentation for the body when using GET, 
and proxies in the middle might not support it.
"""

# from fastapi import FastAPI
# # Import Pydantic's BaseModel
# from pydantic import BaseModel

# app = FastAPI()

# # Create your data model
# class Item(BaseModel):
#     name : str
#     description :str | None = None
#     price :float
#     tax : float | None = None

# @app.post('/items/')
# # Declare it as a parameter o add it to your path operation, declare it the same way you declared path and query parameters
# async def read_items(item: Item):
#     return item

"""
Results
With just that Python type declaration, FastAPI will:

Read the body of the request as JSON.
Convert the corresponding types (if needed).
Validate the data.
If the data is invalid, it will return a nice and clear error, indicating exactly where and what was the incorrect data.
Give you the received data in the parameter item.
As you declared it in the function to be of type Item, you will also have all the editor support (completion, etc) for all of the attributes and their types.
Generate JSON Schema definitions for your model, you can also use them anywhere else you like if it makes sense for your project.
Those schemas will be part of the generated OpenAPI schema, and used by the automatic documentation UIs.
"""

# Use the model - Inside of the function, you can access all the attributes of the model object directly:


"""
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    description : Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.post('/items/')
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
"""


#  Request body + path parameters

"""
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    description : Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.put('/items/')
async def update_item(item_id: int, item:Item):
    return {'item_id' : item_id, **item.dict()}

"""


# Request body + path + query parameters
"""
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
app = FastAPI()
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result"""

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# app = FastAPI()

# # Fake in-memory database
# items_db = {}

# # Pydantic model for data validation
# class Item(BaseModel):
#     name: str
#     price: float
#     description: str | None = None
#     tax: float | None = None


# # 1️⃣ GET - Read all items
# @app.get("/items")
# async def get_items():
#     return {"items": items_db}


# # 2️⃣ GET - Read a specific item (Idempotent)
# @app.get("/items/{item_id}")
# async def get_item(item_id: int):
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return items_db[item_id]


# # 3️⃣ POST - Create a new item (Not Idempotent)
# @app.post("/items", status_code=201)
# async def create_item(item: Item):
#     new_id = len(items_db) + 1
#     items_db[new_id] = item.dict()
#     return {"id": new_id, "item": item}


# # 4️⃣ PUT - Replace an existing item (Idempotent)
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     items_db[item_id] = item.dict()
#     return {"id": item_id, "item": item}


# # 5️⃣ PATCH - Partially update an item (Not Idempotent)
# @app.patch("/ites/{item_id}")
# async def patch_item(item_id: int, item: Item):
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
    
#     # Only update provided fields
#     for key, value in item.dict(exclude_unset=True).items():
#         items_db[item_id][key] = value
    
#     return {"id": item_id, "item": items_db[item_id]}


# # 6️⃣ DELETE - Remove an item (Idempotent)
# @app.delete("/items/{item_id}")
# async def delete_item(item_id: int):
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     del items_db[item_id]
#     return {"message": f"Item {item_id} deleted"}


"""
from datetime import datetime

import logfire

from pydantic import BaseModel

logfire.configure()
logfire.instrument_pydantic()  


class Delivery(BaseModel):
    timestamp: datetime
    dimensions: tuple[int, int]


# this will record details of a successful validation to logfire
m = Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])
print(repr(m.timestamp))
#> datetime.datetime(2020, 1, 2, 3, 4, 5, tzinfo=TzInfo(UTC))
print(m.dimensions)
#> (10, 20)

Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10'])
"""