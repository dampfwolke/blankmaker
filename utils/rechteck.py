import ezdxf
import pathlib # Importiert für Pfad-Operationen

def rechteck_erstellen(length: float, width: float, height: float, output_path_str: str):
    """
    Erstellt eine DXF-Datei mit einem Rechteck und Bemaßungstext.

    Args:
        length (float): Länge des Rechtecks (X-Achse).
        width (float): Breite des Rechtecks (Y-Achse).
        height (float): Höhe des Quaders (Z-Achse).
        output_path_str (str): Der vollständige Pfad (als String) zum Speichern der DXF-Datei.

    Returns:
        tuple: (bool, str) -> (Erfolg, Nachricht)
    """
    try:
        doc = ezdxf.new('R2010')
        msp = doc.modelspace()

        # Rechteck mit den angegebenen Länge und Breite erstellen
        center = (0, 0, -4) # Z-Offset, damit die untere Fläche bei z=-4 liegt
        points = [
            (center[0] - length / 2, center[1] - width / 2, center[2]),
            (center[0] + length / 2, center[1] - width / 2, center[2]),
            (center[0] + length / 2, center[1] + width / 2, center[2]),
            (center[0] - length / 2, center[1] + width / 2, center[2]),
            (center[0] - length / 2, center[1] - width / 2, center[2]), # Schließen der Polylinie
        ]
        msp.add_polyline3d(points, dxfattribs={'layer': 'Roh', 'color': 198})

        # Kopie des Rechtecks für die obere Fläche erstellen
        copy_points = [(x, y, z + height) for x, y, z in points]
        msp.add_polyline3d(copy_points, dxfattribs={'layer': 'Roh', 'color': 198})

        schriftgroesse = 0
        if 0 < length <= 50:
            schriftgroesse = 4
        elif 50 < length <= 75:
            schriftgroesse = 5
        elif 75 < length <= 100:
            schriftgroesse = 7
        elif 100 < length <= 160:
            schriftgroesse = 8
        elif 160 < length <= 210:
            schriftgroesse = 10
        else:
            schriftgroesse = 13

        # Text mit den angegebenen Seitenlängen und Höhe hinzufügen
        text_content = f"X:{length}mm \nY:{width}mm \nZ:{height}mm"
        text_entity = msp.add_text(text_content, dxfattribs={'height': schriftgroesse, 'layer': 'Roh', 'color': 90})

        # Textposition anpassen (z.B. links oben auf der oberen Fläche)
        text_x = -length / 2
        text_y = (width / 2) + 4 # Etwas über der oberen Kante
        text_z = center[2] + height # Auf der Höhe der oberen Fläche
        text_entity.dxf.insert = (text_x, text_y, text_z)
        text_entity.dxf.rotation = 0

        # Verwende pathlib für den Pfad
        file_path = pathlib.Path(output_path_str)

        # Stelle sicher, dass das Elternverzeichnis existiert
        file_path.parent.mkdir(parents=True, exist_ok=True)

        doc.saveas(file_path)
        return True, f"DXF '{file_path}' wurde erfolgreich gespeichert."

    except IOError as e:
        err_msg = f"Fehler beim Speichern der DXF-Datei unter '{file_path}': {e}\n"
        err_msg += "Stellen Sie sicher, dass der Pfad existiert und Sie Schreibrechte haben.\n"
        
        # Versuch, lokal zu speichern
        local_fallback_path = pathlib.Path.cwd() / f"!rohteil_lokal_{length}x{width}x{height}.dxf"
        try:
            doc.saveas(local_fallback_path)
            err_msg += f"DXF wurde stattdessen lokal als '{local_fallback_path}' gespeichert."
            # In diesem Fall ist es immer noch ein "Erfolg" mit einer Anmerkung
            return True, err_msg 
        except Exception as e_local:
            err_msg += f"Fehler auch beim lokalen Speichern: {e_local}"
            return False, err_msg
            
    except ValueError as e: # Falls z.B. ungültige Werte für Längen übergeben werden
        return False, f"Ungültige Eingabewerte: {e}"
        
    except Exception as e:
        return False, f"Ein unerwarteter Fehler ist beim Erstellen/Speichern aufgetreten: {e}"


if __name__ == "__main__":
    # Testaufruf
    test_output_path = pathlib.Path.cwd() / "test_rechteck.dxf" # Speichert im aktuellen Verzeichnis
    success, message = rechteck_erstellen(length=120, width=80, height=30, output_path_str=str(test_output_path))
    if success:
        print(f"Erfolg: {message}")
    else:
        print(f"Fehler: {message}")

    # Test mit einem Pfad, der möglicherweise nicht existiert (nur zur Demonstration des Fallbacks)
    # Vorsicht: Dieser Pfad wird versucht zu erstellen, wenn er nicht existiert!
    # non_existent_dir_path = pathlib.Path("K:/NICHT_EXISTENT_FUER_TEST/test_rechteck_fail.dxf")
    # success, message = rechteck_erstellen(length=50, width=50, height=10, output_path_str=str(non_existent_dir_path))
    # print(f"Zweiter Test: {success}, Nachricht: {message}")