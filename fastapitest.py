from fastapi import FastAPI
from  functions import country_trendline, fit_trendline

from pydantic import BaseModel
from typing import List

class TrendlineInput(BaseModel):
    timestamps: List[int]
    data: List[float]

app = FastAPI()

@app.get("/say_hi")
def say_hi():
    return {"Hi": "There"}


@app.get("/say_hello/{name}")
def say_hello(name):
    return {"Hello": name}

# @app.get("/country_trendline/{country}")
# def calculate_country_trendline(country: str):
#     slope, r_squared = country_trendline(country)
#     return {"slope": slope, "r_squared": r_squared}


@app.post("fit_trendline/")
def calculate_trendline(trendline_input: TrendlineInput):
    slope, r_squared = fit_trendline(trendline_input.timestamps, trendline_input.data)
    return {"slope": slope, "r_squared": r_squared}