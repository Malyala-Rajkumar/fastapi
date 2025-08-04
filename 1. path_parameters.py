
# import asyncio
# # Define an async function
# async def say_hello():
#     print("Hello after 1 second...")
#     await asyncio.sleep(1)
#     print("Hello again!")

# # Main async function
# async def main():
#     await say_hello()
# say_hello()


"""
Properly run it
asyncio.run(say_hello())
"""


# from fastapi import FastAPI

# obj = FastAPI()

# @obj.get('/')
# def main():
#     return 'hello world'

# if __name__ == '__main__':
#     obj.run()"""

"""
Path Parameters
You can declare path "parameters" or "variables" with the same syntax used by Python format strings:
"""

# from fastapi import FastAPI
# app = FastAPI()

# @app.get('/items/{item_id}')
# async def read_item(item_id : int):
#     return {'item_id': item_id}

# from fastapi import FastAPI

# app = FastAPI()
# @app.get("/users/me")
# def read_user_me():
#     return {"user_id": "the current user"}


# @app.get("/users/{user_id}")
# def read_user(user_id: str):
#     return {"user_id": user_id}

"""Order matters"""

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}


# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

"""
Predefined values

If you have a path operation that receives a path parameter, but you want the possible valid path parameter values to be
predefined, you can use a standard Python Enum.
"""

# Create an Enum class

"""
Import Enum and create a sub-class that inherits from `str` and from `Enum`.

By inheriting from str the API docs will be able to know that the values must be of type string and will be able to 
render correctly.

Then create class attributes with fixed values, which will be the available valid values:
"""


# from enum import Enum
# from fastapi import FastAPI
# app = FastAPI()
# class ModelName(str, Enum):
#     alexnet = 'alexnet'
#     resnet = 'resnet'
#     lenet = 'lenet'
# @app.get('/models/{model_name}')
# async def get_model(model_name: ModelName):
#     # if model_name is ModelName.alexnet:
#     if model_name.value == "alexnet":
#         return {'Model Name': model_name, 'message': 'This model is the Deep Learning the FTW!'}
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#     return {"model_name": model_name, "message": "Have some residuals"}