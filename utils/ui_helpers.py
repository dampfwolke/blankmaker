# utils/ui_helpers.py
import pathlib
from PySide6.QtWidgets import QComboBox, QStatusBar # Typ-Hinweise
from typing import Dict, Optional

def populate_combobox_with_subfolders(
    combobox: QComboBox, 
    settings: Dict, 
    settings_key: str, 
    status_bar: Optional[QStatusBar] = None
) -> bool:
    """
    Füllt eine QComboBox mit den Namen der Unterordner aus einem Basispfad,
    der aus den Einstellungen (settings) gelesen wird.

    Args:
        combobox: Die QComboBox, die gefüllt werden soll.
        settings: Das Dictionary mit den geladenen Einstellungen.
        settings_key: Der Schlüssel in den Einstellungen, der den Basispfad enthält.
        status_bar: Optional die QStatusBar für Rückmeldungen.

    Returns:
        bool: True, wenn erfolgreich (oder teilweise erfolgreich mit Warnungen), 
              False, wenn ein kritischer Fehler auftrat (z.B. Pfad nicht konfiguriert).
    """
    combobox.clear()  # Vorherige Einträge löschen

    base_path_str = settings.get(settings_key)

    def show_status(message: str, timeout: int = 7000):
        if status_bar:
            status_bar.showMessage(message, timeout)
        print(f"[UI_HELPER] {message}") # Immer auf Konsole ausgeben

    if not base_path_str:
        show_status(f"Fehler: '{settings_key}' nicht in Einstellungen gefunden.")
        combobox.addItem(f"Fehler: {settings_key} fehlt")
        combobox.setDisabled(True)
        return False

    base_path = pathlib.Path(base_path_str)

    if not base_path.exists():
        show_status(f"Fehler: Pfad '{base_path}' für '{settings_key}' existiert nicht.")
        combobox.addItem(f"Fehler: Pfad nicht gefunden")
        combobox.setDisabled(True)
        return False
    
    if not base_path.is_dir():
        show_status(f"Fehler: Pfad '{base_path}' für '{settings_key}' ist kein Verzeichnis.")
        combobox.addItem(f"Fehler: Kein Ordner")
        combobox.setDisabled(True)
        return False
    
    combobox.setDisabled(False) # Bei Erfolg wieder aktivieren, falls zuvor deaktiviert

    subfolders_found = False
    try:
        for item in base_path.iterdir():
            if item.is_dir():
                combobox.addItem(item.name)
                subfolders_found = True
        
        if not subfolders_found:
            show_status(f"Info: Keine Unterordner in '{base_path}' gefunden.", 5000)
            combobox.addItem("Keine Einträge gefunden") # Platzhalter
        else:
            show_status(f"ComboBox '{combobox.objectName()}' geladen aus '{base_path}'.", 3000)
        return True

    except PermissionError:
        show_status(f"Fehler: Keine Leserechte für Pfad '{base_path}'.")
        combobox.addItem("Fehler: Leserechte")
        combobox.setDisabled(True)
        return False # Hier könnte man argumentieren, dass es true sein sollte, aber mit disabled CB
    except Exception as e:
        show_status(f"Unbekannter Fehler beim Lesen von '{base_path}': {e}")
        combobox.addItem("Fehler: Unbekannt")
        combobox.setDisabled(True)
        return False