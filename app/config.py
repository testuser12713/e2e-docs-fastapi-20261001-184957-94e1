"""Anwendungskonfiguration über pydantic-settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Zentrale Konfiguration.

    Alle Umgebungsvariablen tragen das Präfix ``NOTES_``. Es gibt derzeit keine
    Pflichtvariablen; die Anwendung startet ohne jede Konfiguration.
    """

    model_config = SettingsConfigDict(env_prefix="NOTES_", extra="ignore")
