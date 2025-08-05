# gt: greater than
# ge: greater than or equal
# lt: less than
# le: less than or equal

""""
Query Parameters with a Pydantic Model:- 

Declare the query parameters that you need in a Pydantic model, and then declare the parameter as Query:
"""

# from typing import Annotated, Literal
# from fastapi import FastAPI, Query
# from pydantic import BaseModel, Field

# app = FastAPI()
# class Filterparams(BaseModel):
#     limit: int = Field(100, gt= 0, le= 100)
#     offset:int = Field(0, ge=0)
#     order_by: Literal["created_at", "updated_at"] = "created_at"
#     tags:list[str] = []

# @app.get('/items/')
# async def read_items(filterquery:Annotated[Filterparams, Query()]):
#     return filterquery

"""
If you want, I can show you a real-world example where limit, offset, order_by, and tags are used together to 
fetch filtered and paginated results from a database.

FastAPI will extract the data for each field from the query parameters in the request and 
give you the Pydantic model you defined.
"""


# from fastapi import FastAPI, Query
# from typing_extensions import Annotated, Literal
# from pydantic import BaseModel, Field

# app = FastAPI()

# class FilterParams(BaseModel):
#     model_config = {"extra": "forbid"}
#     limit: int = Field(100, gt=0, le=100)
#     offset: int = Field(0, ge=0)
#     order_by: Literal["created_at", "updated_at"] = "created_at"
#     tags: list[str] = []


# @app.get("/items/")
# async def read_items(filter_query: Annotated[FilterParams, Query()]):
#     return filter_query

"""
If a client tries to send some extra data in the query parameters, they will receive an error response.
Spoiler alert: you can also use Pydantic models to declare cookies and headers, but you will read about that 
later in the tutorial. 🤫
"""