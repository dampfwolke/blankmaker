# utils/input_validators.py
from typing import Tuple, Optional


def calculate_spanntiefe(z_fertig_str: str) -> Tuple[bool, Optional[int]]:
    """
    Berechnet die Spanntiefe basierend auf dem Z-Fertigmaß.
    Die Logik ist: z_fertig - 2, aber mindestens 2, und als ganze Zahl.

    Args:
        z_fertig_str: Der Text aus dem LineEdit le_z_fertig.

    Returns:
        Ein Tupel (Erfolg, Ergebnis).
        Bei Erfolg: (True, berechnete_spanntiefe_als_int)
        Bei Fehler/ungültiger Eingabe: (False, None)
    """
    # Ersetze Komma durch Punkt für die Konvertierung
    processed_str = z_fertig_str.replace(',', '.')

    if not processed_str:
        return False, None

    try:
        z_fertig_val = float(processed_str)

        # Berechne den Wert: z_fertig - 2
        calculated_value = z_fertig_val - 2

        # Stelle sicher, dass der Wert mindestens 2 ist
        final_value = max(2.0, calculated_value)

        # Konvertiere in eine ganze Zahl (Integer)
        return True, int(final_value)

    except ValueError:
        # Wenn die Eingabe keine gültige Zahl ist
        return False, None

def validate_dimensions(
    length_str: str, 
    width_str: str, 
    height_str: str
) -> Tuple[bool, Optional[float], Optional[float], Optional[float], Optional[str]]:
    """
    Validiert die Eingabe-Strings für Länge, Breite und Höhe (Rechteck).
    Konvertiert Kommas zu Punkten, prüft auf leere Strings,
    konvertiert zu float und prüft auf positive Werte.

    Returns:
        Tuple: (Erfolg, Länge, Breite, Höhe, Fehlermeldung)
               Bei Erfolg: (True, float_wert, float_wert, float_wert, None)
               Bei Fehler: (False, None, None, None, "Fehlermeldung als String")
    """
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


def validate_circle_dimensions(
    diameter_str: str, 
    height_str: str
) -> Tuple[bool, Optional[float], Optional[float], Optional[str]]:
    """
    Validiert die Eingabe-Strings für Durchmesser und Höhe (Kreis/Zylinder).
    Konvertiert Kommas zu Punkten, prüft auf leere Strings,
    konvertiert zu float und prüft auf positive Werte.

    Returns:
        Tuple: (Erfolg, Durchmesser, Höhe, Fehlermeldung)
               Bei Erfolg: (True, float_wert, float_wert, None)
               Bei Fehler: (False, None, None, "Fehlermeldung als String")
    """
    processed_diameter_str = diameter_str.replace(',', '.')
    processed_height_str = height_str.replace(',', '.')

    if not all([processed_diameter_str, processed_height_str]):
        return False, None, None, "Eingabe fehlt: Bitte Felder für Durchmesser und Höhe füllen."

    try:
        diameter = float(processed_diameter_str)
        height = float(processed_height_str)
    except ValueError:
        return False, None, None, "Ungültige Eingabe: Bitte gültige Zahlen für Kreis-Maße eingeben."

    if not (diameter > 0 and height > 0): # Höhe kann auch 0 sein, wenn es nur ein 2D Kreis sein soll, aber für Zylinder > 0
        return False, None, None, "Ungültige Kreis-Maße: Durchmesser und Höhe müssen positive Zahlen sein."

    return True, diameter, height, None