import ezdxf
from ezdxf import enums
from pathlib import Path  # Geändert
from typing import Tuple


def kreis_erstellen(diameter: float, height: float, output_path_str: str, base_offset_factor=0.05) -> Tuple[bool, str]:
    """
    Erstellt eine DXF-Datei mit einem Zylinder (zwei Kreise) und Bemaßungstext.

    Args:
        diameter (float): Durchmesser des Kreises in mm.
        height (float): Höhe des Zylinders in mm.
        output_path_str (str): Der vollständige Pfad (als String) zum Speichern der DXF-Datei.
        base_offset_factor (float): Faktor des Radius für Textabstand.

    Returns:
        tuple: (bool, str) -> (Erfolg, Nachricht)
    """
    try:
        doc = ezdxf.new("R2010")
        msp = doc.modelspace()

        radius = diameter / 2
        z_offset1 = -6  # Unterer Kreis
        z_offset2 = height - 6  # Oberer Kreis
        # Kreise zeichnen
        msp.add_circle((0, 0, z_offset1), radius, dxfattribs={'layer': 'Roh', 'color': 198})
        msp.add_circle((0, 0, z_offset2), radius, dxfattribs={'layer': 'Roh', 'color': 198})
        # Dynamische Textgröße (mindestens 1.2 mm, maximal 8 mm)
        text_height = max(1.2, min(diameter * 0.14, 8))

        min_gap_circle_text = text_height * 0.5
        text_gap_from_circle_edge = max(min_gap_circle_text, radius * base_offset_factor)
        text_block_effective_width = text_height  # Vereinfachung, tatsächliche Breite hängt von Zeichen ab
        x_center_for_texts = radius + text_gap_from_circle_edge + (text_block_effective_width / 2)

        diameter_text_str = f"Ø DM = {diameter} mm"
        height_text_str = f"Höhe = {height} mm"

        font_char_aspect_ratio_approx = 0.4

        rendered_length_diameter_text = len(diameter_text_str) * text_height * font_char_aspect_ratio_approx
        rendered_length_height_text = len(height_text_str) * text_height * font_char_aspect_ratio_approx
        desired_gap_between_text_blocks = text_height * 1.0  # Größerer Abstand

        # Y-Positionen relativ zum Mittelpunkt des Kreises (0,0)
        y_center_diameter_text = (rendered_length_height_text / 2) + (desired_gap_between_text_blocks / 2)
        y_center_height_text = -((rendered_length_diameter_text / 2) + (desired_gap_between_text_blocks / 2))

        z_pos = z_offset2  # Text auf Höhe des oberen Kreises
        rotation = 310

        common_text_attribs = {
            'layer': 'Roh',
            'color': 3,  # Grün
            'height': text_height,
            'rotation': rotation,
            'halign': enums.TextHAlign.CENTER,  # Horizontal zentriert
            'valign': enums.TextVAlign.MIDDLE  # Vertikal zentriert zum Einfügepunkt
        }

        # Einfügepunkte für die Texte
        diameter_text_insert_point = (x_center_for_texts, y_center_diameter_text, z_pos)
        msp.add_text(
            diameter_text_str,
            dxfattribs=common_text_attribs
        ).set_placement(diameter_text_insert_point,
                        align=enums.TextEntityAlignment.MIDDLE_CENTER)  # Explizite Ausrichtung

        height_text_insert_point = (x_center_for_texts, y_center_height_text, z_pos)
        msp.add_text(
            height_text_str,
            dxfattribs=common_text_attribs
        ).set_placement(height_text_insert_point,
                        align=enums.TextEntityAlignment.MIDDLE_CENTER)  # Explizite Ausrichtung

        # Verwende pathlib für den Pfad
        file_path = Path(output_path_str)  # Geändert

        # Stelle sicher, dass das Elternverzeichnis existiert
        file_path.parent.mkdir(parents=True, exist_ok=True)

        doc.saveas(file_path)
        return True, f"Kreis-DXF '{file_path}' wurde erfolgreich gespeichert."

    except IOError as e:
        err_msg = f"Fehler beim Speichern der Kreis-DXF-Datei unter '{file_path}': {e}\n"
        err_msg += "Stellen Sie sicher, dass der Pfad existiert und Sie Schreibrechte haben.\n"

        local_fallback_path = Path.cwd() / f"!rohteil_kreis_lokal_{diameter}x{height}.dxf"  # Geändert
        try:
            doc.saveas(local_fallback_path)
            err_msg += f"Kreis-DXF wurde stattdessen lokal als '{local_fallback_path}' gespeichert."
            return True, err_msg
        except Exception as e_local:
            err_msg += f"Fehler auch beim lokalen Speichern der Kreis-DXF: {e_local}"
            return False, err_msg

    except ValueError as e:
        return False, f"Ungültige Eingabewerte für Kreis: {e}"

    except Exception as e:
        return False, f"Ein unerwarteter Fehler ist beim Erstellen/Speichern des Kreises aufgetreten: {e}"


if __name__ == "__main__":
    test_output_path = Path.cwd() / "kreis.dxf"  # Geändert
    success, message = kreis_erstellen(diameter=80, height=20, output_path_str=str(test_output_path))
    if success:
        print(f"Erfolg: {message}")
    else:
        print(f"Fehler: {message}")