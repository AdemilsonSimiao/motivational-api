from fastapi import FastAPI
import random

app = FastAPI()

phrases = [
    "Believe in yourself!",
    "Keep pushing forward!",
    "You are stronger than you think.",
    "Every day is a fresh start.",
    "Stay positive, work hard, make it happen."
]
@app.get("/")
def read_root():
    return {"message": random.choice(phrases)}