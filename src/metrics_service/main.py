#Import FastAPI from fastapi module
from fastapi import FastAPI

#Initialize FastAPI app
app = FastAPI(title="Metrics Service", description="A service for ingesting and alerting metrics", version="1.0.0")

#Root endpoint that returns simple JSON response
@app.get("/")
def root():
    return {"Hello": "World"}

#Endpoint that returns message indicating user is in docs section
@app.get("/Docs")
def docs():
    return {"message": "You are in docs section"}


@app.get("HealthCheck")
def health_check():
    return {"status": "healthy"}  



