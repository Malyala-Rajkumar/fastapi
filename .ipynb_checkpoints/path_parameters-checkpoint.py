# import asyncio

# # Define an async function
# async def say_hello():
#     print("Hello after 1 second...")
#     await asyncio.sleep(1)
#     print("Hello again!")

# # Main async function
# # async def main():
# #     await say_hello()
# # say_hello()


# Properly run it
# asyncio.run(say_hello())

# from fastapi import FastAPI

# obj = FastAPI()

# @obj.get('/')
# def main():
#     return 'hello world'

# if __name__ == '__main__':
#     obj.run()

'''
Path Parameters
You can declare path "parameters" or "variables" with the same syntax used by Python format strings:
'''

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
"""

