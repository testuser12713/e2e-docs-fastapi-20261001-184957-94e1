"""Tests für DELETE /notes/{id}."""

from fastapi.testclient import TestClient

from app.main import app
from app.schemas import NoteCreate
from app.storage import store


def test_delete_known_note_returns_204_and_removes_it() -> None:
    note = store.create(NoteCreate(titel="Löschen", inhalt="Weg"))
    note_id = note.id

    with TestClient(app) as client:
        response = client.delete(f"/notes/{note_id}")

    assert response.status_code == 204
    assert store.get(note_id) is None


def test_delete_unknown_note_returns_404() -> None:
    with TestClient(app) as client:
        response = client.delete("/notes/999999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Notiz nicht gefunden"}
