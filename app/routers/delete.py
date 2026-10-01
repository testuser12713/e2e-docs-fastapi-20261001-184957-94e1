"""Router für das Löschen von Notizen (DELETE /notes/{id})."""

from fastapi import APIRouter, HTTPException, Response

from app.storage import store

router = APIRouter()


@router.delete("/notes/{id}", status_code=204)
def delete_note(id: int) -> Response:
    if not store.delete(id):
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
    return Response(status_code=204)
