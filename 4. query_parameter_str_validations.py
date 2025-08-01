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

from fastapi import FastAPI, Query
from typing import Annotated
import re 
app = FastAPI()
@app.get('/items/')
def read_items(
    q: Annotated[int|None, Query(min_length = 3, max_length= 50,)]= None):

    results = {'items' : [{'item_id': 'Magic Box'}, {'item_id': 'Bottle'}]}
    if q:
        results.update({'q': q})
    return results

if __name__ == "__main__":
    app.run()


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


""" Required parameters """
























