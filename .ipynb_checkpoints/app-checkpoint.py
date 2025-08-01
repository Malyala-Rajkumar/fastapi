# from fastapi import FastAPI
# from typing import Union
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# @app.get('/')
# def read_root():
#     return {'Hello' : 'World'}

# @app.get('/items/{item_id}')
# def read_item(item_id: int, q:Union[str, None] = None):
#     return {'item_id': item_id, 'q': q}

# @app.put('/items/{item_id}')
# def update_item(item_id: int, item:Item):
#     return {'item_name': item.name, 'item_id': item_id, 'item_price':item.price}

# if __name__ == '__main__':
#     app.run()

# def get_full_name(first_name, last_name):
#     full_name = first_name.title() + " " + last_name.title()
#     return full_name


# print(get_full_name("john", "doe"))

import asyncio
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
return {"message": "Hello, World!"}

async def run_server():
config = uvicorn.Config(app, host="127.0.0.1", port=8000)
server = uvicorn.Server(config)
await server.serve()

asyncio.get_event_loop().create_task(run_server())
