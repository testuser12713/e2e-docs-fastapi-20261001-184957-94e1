"""Router für Lese-Endpunkte (GET /notes und GET /notes/{id})."""

from fastapi import APIRouter, HTTPException

from app.schemas import Note
from app.storage import store

router = APIRouter()


@router.get("/notes", response_model=list[Note])
def list_notes(tag: str | None = None) -> list[Note]:
    notes = store.list()
    if tag is None:
        return notes
    return [note for note in notes if tag in note.tags]


@router.get("/notes/{id}", response_model=Note)
def get_note(id: int) -> Note:
    note = store.get(id)
    if note is None:
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
    return note
