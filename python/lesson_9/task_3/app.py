from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root() -> str:
    return "hello, world"