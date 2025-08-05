# from fastapi import FastAPI
# from typing import Union

# app = FastAPI()

# @app.get('/items/')
# async def read_items(q: Union[str, None] = None):
#     results = {"items" : [{'item_id': 'Bottle'}, {'item_id': 'Pen'}]}
#     if q :
#         results.update({'q': q})
#     return results 
 
"""
Additional validation: 
Annotated → A Python 3.9+ feature that allows combining type hints with extra metadata 
(in this case, the FastAPI Query configuration).

We are going to enforce that even though q is optional, whenever it is provided, its length doesn't exceed 50 characters.

Import Query and Annotated
To achieve that, first import:
Query from fastapi
Annotated from typing
"""

# from typing import Annotated
# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get('/items/')
# async def read_items(q:Annotated[str|None, Query(max_length= 5)] = None):
#     results = {'items' : [{'item_id': 'Magic Box'}, {'item_id': 'Bottle'}]}
#     if q:
#         results.update({'q': q})
#     return results

# if __name__ == "__main__":
#     app.run()

"""
Add more validations:
You can also add a parameter `min_length`:
"""

# from fastapi import FastAPI, Query
# from typing import Annotated

# app = FastAPI()
# @app.get('/items/')
# async def read_items(q: Annotated[str|None, Query(min_length= 5, max_length= 50)]= None):
#     results = {'items' : [{'item_id': 'Magic Box'}, {'item_id': 'Bottle'}]}
#     if q:
#         results.update({'q': q})
#     return results

# if __name__ == "__main__":
#     app.run()

# Add regular expression


"""
Add regular expressions

"""

# from fastapi import FastAPI, Query
# from typing import Annotated
# import re 
# app = FastAPI()
# @app.get('/items/')
# def read_items(
#     q: Annotated[int|None, Query(min_length = 3, max_length= 50,)]= None):

#     results = {'items' : [{'item_id': 'Magic Box'}, {'item_id': 'Bottle'}]}
#     if q:
#         results.update({'q': q})
#     return results

# if __name__ == "__main__":
#     app.run()


"""
Pydantic v1 `regex` instead of `pattern`
"""

# from typing import Annotated
# from fastapi import FastAPI, Query
# app = FastAPI()

# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None, Query(min_length=3, max_length=50, regex="^fixedquery$")
#     ] = None,):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

"""Default values"""

# from fastapi import FastAPI, Query 
# from typing import Annotated

# app = FastAPI()
# @app.get('/items/')
# async def read_items(q:Annotated[str, Query(min_length=3)] = 'fixedquery'):
#     results = {'items' : [{'item_id': 'Magic Box'}, {'item_id': 'Bottle'}]}
#     if q:
#         results.update({'q': q})
#     return results

# if __name__ == "__main__":
#     app.run()


""" 
Required parameters :- 
When we don't need to declare more validations or metadata, we can make the q query parameter required just by not declaring a default value, like:
"""

# from typing import Annotated
# from fastapi import FastAPI, Query

# app =FastAPI()
# @app.get('/')
# async def read_items(q: Annotated[str, Query(min_length= 3)]):
#     results = {'items' : [{'item_id': 'Magic Box'}, {'item_id': 'Bottle'}]}
#     if q:
#         results.update({'q': q})
#     return results

"""
Refer to fastapi notes
"""

"""
Declare more metadata:- 
You can add more information about the parameter.
That information will be included in the generated OpenAPI and used by the documentation user interfaces and external tools.
"""


# from fastapi import FastAPI, Query
# from typing_extensions import Annotated

# obj = FastAPI()
# @obj.get('/read_items/')
# async def read_items(q: Annotated[str|None, Query(min_length= 3, title="This is the read Items function", 
#                     description='It is all having all the query parameter string vallidation of the data')] = None):
#     results = {'items' : [{'item_id': 'Magic Box'}, {'item_id': 'Bottle'}]}
#     if q:
#         results.update({'q': q})
#     return results


"""
Alias parameters
"""

# from fastapi import FastAPI, Query
# from typing import Annotated

# app =FastAPI()
# @app.get('/items')
# async def read_items(q:Annotated[str|None, Query(alias= 'item-query')] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

"""
Deprecating parameters
Now let's say you don't like this parameter anymore.

You have to leave it there a while because there are clients using it, but you want the docs to clearly show it as deprecated.

Then pass the parameter `deprecated=True` to `Query`:
"""

# from turtle import title
# from typing_extensions import Annotated
# from fastapi import FastAPI, Query
# app =FastAPI()
# @app.get('/items/')
# async def read_items(q: Annotated[str|None,
#                     Query(alias= 'item-query',
#                     title='Query string',
#                     description="Query string for the items to search in the database that have a good match",
#                     min_length=3,
#                     max_length=50,
#                     pattern="^fixedquery$",
#                     deprecated=True,)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


"""
Exclude parameters from OpenAPI:- 
To exclude a query parameter from the generated OpenAPI schema (and thus, from the automatic documentation systems), set the parameter 
include_in_schema of Query to False:
"""

from typing import Annotated
from fastapi import FastAPI, Query
app = FastAPI()
@app.get("/items/")

async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}