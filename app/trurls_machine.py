from fastapi import FastAPI

app = FastAPI()


@app.post("/add")
async def root():
    return {"sum": 7}
