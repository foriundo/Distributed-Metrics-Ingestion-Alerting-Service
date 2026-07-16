from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/Docs")
def docs():
    return {"message": "You are in docs section"}