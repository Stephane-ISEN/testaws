from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def test():
    return "Hello World!"
@app.get("/test")
    return "test"
