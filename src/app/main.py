from fastapi import FastAPI

from app.api import ping
from app.db import engine, metadata, database

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)

# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Optional[bool] = None


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


# @app.post("/items/")
# def create_item(item: Item):
#     return item


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, "item_name": item.name, "item_price": item.price, "item_is_offer": item.is_offer}