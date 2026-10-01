"""Router für das Anlegen von Notizen (POST /notes)."""

from fastapi import APIRouter

from app.schemas import Note, NoteCreate
from app.storage import store

router = APIRouter()


@router.post("/notes", response_model=Note, status_code=201)
def create_note(note: NoteCreate) -> Note:
    return store.create(note)
