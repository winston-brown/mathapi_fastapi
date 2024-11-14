from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

class NumbersRequest(BaseModel):
    numbers: List[float] = Field(min_length=1, max_length=100)

app = FastAPI()

@app.post("/average")
def calculate_average(numbers: NumbersRequest):
    try:
        average = sum(numbers.numbers) / len(numbers.numbers)
        return {"average": average}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
