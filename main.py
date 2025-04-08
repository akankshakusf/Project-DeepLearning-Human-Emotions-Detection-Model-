from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input_Item(BaseModel):
    name:str
    price:int 
    discount:int

class Output_Item(BaseModel):
    name:str
    selling_price : int

@app.get("/entry")
def read_root():
    return {"Hello": "World"}

@app.post("/items/", response_model = Output_Item)
def add_item(item: Input_Item):
    selling_price = item.price =item.discount
    return {"name": item.name, "selling_price":selling_price}