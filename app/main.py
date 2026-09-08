from app.routers.books import router as books_router
from fastapi import FastAPI, HTTPException
from app.database import engine, Base
from fastapi.responses import RedirectResponse
from app import utils

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(books_router)

@app.get("/")
def home():
    return RedirectResponse("/books")

@app.get("/add")
def add_numbers(num1: int, num2: int):
    result = utils.add(num1, num2)
    return {"result": result}

@app.get("/subtract")
def subtract_numbers(num1: int, num2: int):
    result = utils.subtract(num1, num2)
    return {"result": result}



@app.get("/multiply")
def multiply_numbers(num1: int, num2: int):
    result = utils.multiply(num1, num2)
    return {"result": result}

@app.get("/divide")
def divide_numbers(num1: int, num2: int):
    try:
        result = utils.divide(num1, num2)
        return {"result": result}

    except (ValueError, ZeroDivisionError) as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "API is healthy"}
