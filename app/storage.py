"""In-Memory-Speicher für Notizen."""

from datetime import UTC, datetime

from app.schemas import Note, NoteCreate


class NoteStore:
    """Einfacher In-Memory-Speicher (kein Datenbank) für Notizen."""

    def __init__(self) -> None:
        self._notes: dict[int, Note] = {}
        self._next_id = 1

    def create(self, note: NoteCreate) -> Note:
        """Legt eine Notiz an und vergibt ``id`` und ``erstellt_am`` serverseitig."""
        new_note = Note(
            id=self._next_id,
            titel=note.titel,
            inhalt=note.inhalt,
            tags=note.tags,
            erstellt_am=datetime.now(UTC),
        )
        self._notes[self._next_id] = new_note
        self._next_id += 1
        return new_note

    def list(self) -> list[Note]:
        """Gibt alle gespeicherten Notizen zurück."""
        return list(self._notes.values())

    def get(self, id: int) -> Note | None:
        """Gibt die Notiz mit der gegebenen ``id`` zurück oder ``None``."""
        return self._notes.get(id)

    def delete(self, id: int) -> bool:
        """Löscht die Notiz mit der gegebenen ``id``; gibt an, ob gelöscht wurde."""
        if id in self._notes:
            del self._notes[id]
            return True
        return False


store = NoteStore()
