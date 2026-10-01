"""Tests für die Lese-Endpunkte (GET /notes und GET /notes/{id})."""

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.schemas import NoteCreate
from app.storage import store


@pytest.fixture()
def client() -> TestClient:
    store._notes.clear()
    store._next_id = 1
    return TestClient(app)


def test_list_notes_returns_all_notes(client: TestClient) -> None:
    store.create(NoteCreate(titel="Erste", inhalt="Inhalt 1", tags=["arbeit"]))
    store.create(NoteCreate(titel="Zweite", inhalt="Inhalt 2", tags=["privat"]))

    response = client.get("/notes")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert [note["titel"] for note in data] == ["Erste", "Zweite"]


def test_list_notes_is_empty_when_no_notes(client: TestClient) -> None:
    response = client.get("/notes")

    assert response.status_code == 200
    assert response.json() == []


def test_list_notes_with_tag_filter_matching(client: TestClient) -> None:
    store.create(NoteCreate(titel="A", tags=["xyz"]))
    store.create(NoteCreate(titel="B", tags=["abc"]))
    store.create(NoteCreate(titel="C", tags=["xyz", "abc"]))

    response = client.get("/notes", params={"tag": "xyz"})

    assert response.status_code == 200
    data = response.json()
    assert [note["titel"] for note in data] == ["A", "C"]


def test_list_notes_with_tag_filter_no_match(client: TestClient) -> None:
    store.create(NoteCreate(titel="A", tags=["abc"]))

    response = client.get("/notes", params={"tag": "xyz"})

    assert response.status_code == 200
    assert response.json() == []


def test_get_note_known_id_returns_200(client: TestClient) -> None:
    note = store.create(NoteCreate(titel="Bekannt", inhalt="Inhalt", tags=["a"]))

    response = client.get(f"/notes/{note.id}")

    assert response.status_code == 200
    assert response.json()["id"] == note.id
    assert response.json()["titel"] == "Bekannt"


def test_get_note_unknown_id_returns_404(client: TestClient) -> None:
    response = client.get("/notes/999999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Notiz nicht gefunden"}
