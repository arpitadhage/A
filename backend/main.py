from fastapi import FastAPI

app = FastAPI(
    title="Datasmith Agent",
    version="1.0.0"
)


@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "Datasmith Agent Backend"
    }