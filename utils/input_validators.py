# utils/input_validators.py
from typing import Tuple, Optional

def validate_dimensions(
    length_str: str, 
    width_str: str, 
    height_str: str
) -> Tuple[bool, Optional[float], Optional[float], Optional[float], Optional[str]]:
    """
    Validiert die Eingabe-Strings für Länge, Breite und Höhe.
    Konvertiert Kommas zu Punkten, prüft auf leere Strings,
    konvertiert zu float und prüft auf positive Werte.

    Returns:
        Tuple: (Erfolg, Länge, Breite, Höhe, Fehlermeldung)
               Bei Erfolg: (True, float_wert, float_wert, float_wert, None)
               Bei Fehler: (False, None, None, None, "Fehlermeldung als String")
    """
    # Komma durch Punkt ersetzen, falls noch nicht durch Validator geschehen
    # oder falls die Eingabe von einer anderen Quelle kommt.
    processed_length_str = length_str.replace(',', '.')
    processed_width_str = width_str.replace(',', '.')
    processed_height_str = height_str.replace(',', '.')

    if not all([processed_length_str, processed_width_str, processed_height_str]):
        return False, None, None, None, "Eingabe fehlt: Bitte alle Felder für Länge, Breite und Höhe füllen."

    try:
        length = float(processed_length_str)
        width = float(processed_width_str)
        height = float(processed_height_str)
    except ValueError:
        return False, None, None, None, "Ungültige Eingabe: Bitte gültige Zahlen für Maße eingeben."

    if not (length > 0 and width > 0 and height > 0):
        return False, None, None, None, "Ungültige Maße: Länge, Breite und Höhe müssen positive Zahlen sein."

    return True, length, width, height, None