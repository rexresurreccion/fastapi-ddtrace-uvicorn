from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(timestamp):
    return {"webapp-extension": f"Timestamp {timestamp}"}


