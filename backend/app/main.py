import datetime
import math
import random
from typing import Union

import numpy as np
from fastapi import FastAPI

app = FastAPI()

now = datetime.datetime.now()
minute = datetime.timedelta(days=0,seconds=5,microseconds=0)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/widget/{name}")
def read_item(name: str):
    timestampList = [(now - (datetime.timedelta(days=0,seconds=5,microseconds=0) * i)).strftime("%H:%M:%S") for i in range(100)]
    data = {
        "name": name,
        "type": 'Graph',
        "value": '10%',
        "data": [random.randint(1,100) for _ in range(100)],
        "timestamp": timestampList
          
    }
    return {"data": data}