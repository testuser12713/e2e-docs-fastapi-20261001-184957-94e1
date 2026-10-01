# Notizen-REST-API

Eine kleine REST-API in Python mit FastAPI und Pydantic v2, die Notizen
(`id`, `titel`, `inhalt`, `tags`, `erstellt_am`) in einem In-Memory-Speicher
verwaltet. Es wird keine Datenbank und kein externer Dienst benötigt — die API
startet sofort und alle Endpunkte sind ohne weitere Einrichtung nutzbar.

## Tech Stack

- **Sprache**: Python
- **Framework**: FastAPI
- **Validierung**: Pydantic v2
- **Konfiguration**: pydantic-settings
- **Speicher**: In-Memory (keine Datenbank)
- **Tests**: pytest + FastAPI TestClient

## Installation

```bash
python -m pip install -e .
```

Für die Entwicklung zusätzlich:

```bash
python -m pip install -e ".[dev]"
```

## Start

Im Repo-Root:

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Danach ist die API unter `http://localhost:8000` erreichbar. Die interaktive
Dokumentation (Swagger UI) liegt unter `http://localhost:8000/docs`.

## Endpunkte

| Methode | Pfad           | Beschreibung                                           |
|---------|----------------|--------------------------------------------------------|
| GET     | `/health`      | Health-Check, liefert `{"status": "ok"}`               |
| POST    | `/notes`       | Legt eine Notiz an (Body: `NoteCreate`)                |
| GET     | `/notes`       | Listet alle Notizen; optionaler Filter `?tag=<str>`    |
| GET     | `/notes/{id}`  | Liefert eine einzelne Notiz (404 bei unbekannter `id`) |
| DELETE  | `/notes/{id}`  | Löscht eine Notiz (404 bei unbekannter `id`)           |

### Datenform `Note`

```json
{
  "id": 1,
  "titel": "Einkaufen",
  "inhalt": "Milch und Brot",
  "tags": ["privat"],
  "erstellt_am": "2026-10-01T12:00:00Z"
}
```

- `id` wird fortlaufend ab 1 serverseitig vergeben.
- `erstellt_am` wird serverseitig als `datetime.now(timezone.utc)` gesetzt
  (ISO-8601 UTC).

### Eingabedaten `NoteCreate`

```json
{
  "titel": "Einkaufen",
  "inhalt": "Milch und Brot",
  "tags": ["privat"]
}
```

- `titel`: Pflicht, 1–100 Zeichen.
- `inhalt`: optional, Default `""`.
- `tags`: optional, Default `[]`, maximal 5 Einträge.

### Beispiele

```bash
# Anlegen
curl -X POST http://localhost:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"titel": "Einkaufen", "inhalt": "Milch und Brot", "tags": ["privat"]}'

# Alle Notizen
curl http://localhost:8000/notes

# Nach Tag filtern
curl "http://localhost:8000/notes?tag=privat"

# Einzelne Notiz
curl http://localhost:8000/notes/1

# Löschen
curl -X DELETE http://localhost:8000/notes/1
```

## Features

- Health-Check unter `/health`
- Notizen anlegen, lesen, filtern und löschen
- Pydantic-v2-Validierung mit verständlichen Fehlermeldungen (422)
- In-Memory-Speicher ohne Datenbank-Setup
- Konfiguration über pydantic-settings mit dem Präfix `NOTES_` (keine Pflichtvariablen)

## Tests

```bash
python -m pytest
```
