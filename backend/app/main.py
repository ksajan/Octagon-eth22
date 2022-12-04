import datetime
import math
import random
import time

import pandas as df
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# wd = webdriver.Chrome(options=chrome_options)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
now = datetime.datetime.now()
minute = datetime.timedelta(days=0, seconds=5, microseconds=0)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/widget/{name}")
def read_item(name: str):
    timestampList = [
        (now - (datetime.timedelta(days=0, seconds=5, microseconds=0) * i)).strftime(
            "%H:%M:%S"
        )
        for i in range(10)
    ]
    data = {
        "name": name,
        "type": "Graph",
        "value": "10%",
        "data": [random.randint(1, 100) for _ in range(10)],
        "timestamp": timestampList,
    }
    return {"data": data}


@app.get("/dune/{name}")
def read_item(name: str):
    # wd.get("https://dune.com/queries/1620054")
    time.sleep(2)
    # html = wd.page_source
    # s = df.read_html(html)
    # print(s)
    return {"data": [random.randint(1, 100) for _ in range(10)]}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8002,
        reload=True,
        debug=True,
    )