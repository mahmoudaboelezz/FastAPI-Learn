from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    # serve index.html
    index = open("index.html", "r")
    return index.read()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
