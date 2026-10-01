"""Router für Lese-Endpunkte (GET /notes und GET /notes/{id})."""

from fastapi import APIRouter, HTTPException

from app.schemas import Note

router = APIRouter()


@router.get("/notes", response_model=list[Note])
def list_notes(tag: str | None = None) -> list[Note]:
    raise HTTPException(status_code=501, detail="GET /notes wird von #3 implementiert")


@router.get("/notes/{id}", response_model=Note)
def get_note(id: int) -> Note:
    raise HTTPException(status_code=501, detail="GET /notes/{id} wird von #3 implementiert")
