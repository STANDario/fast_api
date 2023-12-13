from fastapi import FastAPI

from src.routes import contacts


app = FastAPI()


app.include_router(contacts.router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Hi! Thank you for visiting the site :)"}