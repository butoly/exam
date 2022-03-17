# http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc
from typing import Optional
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
import pandas as pd
from database import Database
from drawer import Drawer
from calculator import Calculator

app = FastAPI()
db = Database()
drawer = Drawer()
calculator = Calculator()


@app.get("/getContinents")
def get_continents_list():
    data = db.getData()
    continent_list = data["continent"].drop_duplicates().dropna()
    continent_list = list(continent_list)
    return {"continent_list": continent_list}


@app.get("/getDiagram/{continent}")
async def get_diagram(continent: str):
    data = calculator.get_total_cases_by_country(continent, db.getData())
    picture = drawer.drawDiagram(data)
    return {"continent": continent}


@app.get("/getCountries/{continent}")
async def get_countries(continent: str):
    data = calculator.get_avg_country(continent, db.getData())
    return {"data": data}


@app.post("/uploadFile/")
async def create_upload_file(file: UploadFile):
     data = pd.read_csv(file.filename)
     db.setData(data)
     return {"token": "token"}

