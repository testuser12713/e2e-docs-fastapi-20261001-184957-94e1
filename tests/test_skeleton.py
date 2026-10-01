"""Tests für das FastAPI-Grundgerüst."""

from datetime import UTC, datetime

from fastapi.testclient import TestClient

from app.main import app
from app.schemas import NoteCreate
from app.storage import store


def test_health_returns_200_ok() -> None:
    with TestClient(app) as client:
        response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_store_create_assigns_id_and_erstellt_am() -> None:
    note = store.create(NoteCreate(titel="Test", inhalt="Inhalt", tags=["a"]))

    assert isinstance(note.id, int)
    assert note.id >= 1
    assert isinstance(note.erstellt_am, datetime)
    assert note.erstellt_am.tzinfo is not None
    assert note.erstellt_am <= datetime.now(UTC)
