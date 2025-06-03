# utils/get_settings.py

import json
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "settings/einstellungen.json"

def load_settings() -> dict:
    """Lädt die Konfigurationsdaten aus der JSON-Datei."""
    try:
        with CONFIG_PATH.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Konfigurationsdatei nicht gefunden: {CONFIG_PATH}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Fehler beim Parsen der Konfigurationsdatei: {e}")

def get_stylesheet_path(settings: dict) -> Path | None:
    """Ermittelt den Pfad zum Stylesheet basierend auf der Einstellung. Gibt None zurück, wenn leer."""
    style_name = settings.get("styles", "").strip()
    raw_template = settings.get("stylesheet", "")

    if not style_name or not raw_template:
        return None  # Kein Stylesheet gewünscht oder definiert

    style_path = raw_template.format(styles=style_name)
    path = Path(style_path)
    return path if path.exists() else None

def get_pfad_from_template(settings: dict, kw: int, wochentag: str) -> str:
    """Erstellt den Rohteilpfad anhand des Templates."""
    base_path = settings.get("nc_base_path", "")
    projekt = settings.get("projekt_prefix", "")
    nutzer = settings.get("nutzername", "")
    template = settings.get("weitere_einstellungen", {}).get(
        "pfad_template", "{base_path}/{projekt}-KW{kw}/{nutzer}/{wochentag}"
    )
    return template.format(
        base_path=base_path,
        projekt=projekt,
        kw=kw,
        nutzer=nutzer,
        wochentag=wochentag
    )
