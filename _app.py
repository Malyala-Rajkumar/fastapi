"""
This is the Main understanding of the FastAPO base Model    
"""

# from fastapi import FastAPI
# from typing import Union
# from pydantic import BaseModel

# a = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# @a.get('/')
# def read_root():
#     return {'Hello' : 'World'}

# @a.get('/items/{item_id}')
# def read_item(item_id: int, q:Union[str, None] = None):
#     return {'item_id': item_id, 'q': q}

# @a.put('/items/{item_id}')
# def update_item(item_id: int, item:Item):
#     return {'item_name': item.name, 'item_id': item_id, 'item_price':item.price}

# if __name__ == '__main__':
#     a.run()

# def get_full_name(first_name, last_name):
#     full_name = first_name.title() + " " + last_name.title()
#     return full_name


# print(get_full_name("john", "doe"))

"""
Generic types with type parameters¶

There are some data structures that can contain other values, like dict, list, set and tuple. And the internal values can have their own type too.

These types that have internal types are called "generic" types. And it's possible to declare them, even with their internal types.

To declare those types and the internal types, you can use the standard Python module typing. It exists specifically to support these type hints.
"""

"""
Dict
To define a dict, you pass 2 type parameters, separated by commas.

The first type parameter is for the keys of the dict.

The second type parameter is for the values of the dict:
"""

# def process_items(prices: dict[str, float]):
#     for item_name, item_price in prices.items():
#         print(item_name)
#         print(item_price)

# from typing import Optional
# def say_hi(name: Optional[str] = None):
#     if name is not None:
#         print(f"Hey {name}!")
#     else:
#         print("Hello World")

# say_hi()
# class Person:
#     def __init__(self, name: str):
#         self.name = name


# def get_person_name(one_person: Person):
#     return one_person.name

# p = Person("Rajkumar")
# print(get_person_name(p))  

"""
#from datetime import datetime
#from pydantic import BaseModel
# class User(BaseModel):
#     id: int
#     name: str = "John Doe"
#     signup_ts: datetime | None = None
#     friends: list[int] = []
# external_data = {
#     "id": "123",
#     "signup_ts": "2017-06-01 12:22",
#     "friends": [1, "2", b"3"],
# }
# user = User(**external_data)
# print(user)
# # > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
# print(user.id)
# # > 123
"""