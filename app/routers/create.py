"""Router für das Anlegen von Notizen (POST /notes)."""

from fastapi import APIRouter, HTTPException

from app.schemas import Note, NoteCreate

router = APIRouter()


@router.post("/notes", response_model=Note, status_code=201)
def create_note(note: NoteCreate) -> Note:
    raise HTTPException(status_code=501, detail="POST /notes wird von KAN-63 implementiert")
