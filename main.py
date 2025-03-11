from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return " Welcome To Genamplify Employee management system"

@app.get("/about")
def about():
    return "This app have all the data related to Genamplify Employees"

@app.get("/details/{id}")
def details(id:int):
    if id == 1:
        return "this is detials related to employee 1"
