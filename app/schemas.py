"""Pydantic-v2-Modelle für Notizen."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class NoteCreate(BaseModel):
    """Eingabedaten zum Anlegen einer Notiz."""

    model_config = ConfigDict(str_strip_whitespace=True)

    titel: str = Field(..., min_length=1, max_length=100)
    inhalt: str = ""
    tags: list[str] = Field(default_factory=list)

    @field_validator("titel")
    @classmethod
    def titel_not_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("titel darf nicht leer sein")
        return value

    @field_validator("tags")
    @classmethod
    def tags_at_most_five(cls, value: list[str]) -> list[str]:
        if len(value) > 5:
            raise ValueError("höchstens 5 Tags erlaubt")
        return value


class Note(BaseModel):
    """Eine gespeicherte Notiz inklusive serverseitig vergebener Felder."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    titel: str
    inhalt: str
    tags: list[str]
    erstellt_am: datetime
