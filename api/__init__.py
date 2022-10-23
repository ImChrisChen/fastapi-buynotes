from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from api import user, account_note, account_type

app = FastAPI()

app.router.prefix = '/api'

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,  # https://fastapi.tiangolo.com/zh/tutorial/cors/
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(account_note.router)
app.include_router(account_type.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
