"""Tests für POST /notes."""

from fastapi.testclient import TestClient

from app.main import app


def test_create_valid_note_returns_201_with_id_and_erstellt_am() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/notes",
            json={"titel": "Einkaufsliste", "inhalt": "Milch, Brot", "tags": ["einkauf"]},
        )
    assert response.status_code == 201
    body = response.json()
    assert isinstance(body["id"], int) and body["id"] >= 1
    assert body["titel"] == "Einkaufsliste"
    assert body["inhalt"] == "Milch, Brot"
    assert body["tags"] == ["einkauf"]
    assert body["erstellt_am"] is not None


def test_create_without_titel_returns_422() -> None:
    with TestClient(app) as client:
        response = client.post("/notes", json={"inhalt": "ohne Titel"})
    assert response.status_code == 422


def test_create_with_empty_titel_returns_422() -> None:
    with TestClient(app) as client:
        response = client.post("/notes", json={"titel": ""})
    assert response.status_code == 422


def test_create_with_titel_101_chars_returns_422() -> None:
    with TestClient(app) as client:
        response = client.post("/notes", json={"titel": "a" * 101})
    assert response.status_code == 422


def test_create_with_six_tags_returns_422() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/notes", json={"titel": "Titel", "tags": ["a", "b", "c", "d", "e", "f"]}
        )
    assert response.status_code == 422
