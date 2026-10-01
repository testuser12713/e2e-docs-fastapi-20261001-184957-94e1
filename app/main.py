"""FastAPI-Anwendung der Notizen-API."""

from fastapi import FastAPI

from app.routers import create, delete, read

app = FastAPI(title="Notizen-API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(create.router)
app.include_router(read.router)
app.include_router(delete.router)
