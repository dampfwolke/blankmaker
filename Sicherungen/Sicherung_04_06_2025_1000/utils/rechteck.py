import ezdxf


def rechteck_erstellen(length, width, height):
    doc = ezdxf.new('R2010')
    msp = doc.modelspace()

    # Rechteck mit den angegebenen Länge und Breite erstellen
    center = (0, 0, -4)
    points = [
        (center[0] - length / 2, center[1] - width / 2, center[2]),
        (center[0] + length / 2, center[1] - width / 2, center[2]),
        (center[0] + length / 2, center[1] + width / 2, center[2]),
        (center[0] - length / 2, center[1] + width / 2, center[2]),
        (center[0] - length / 2, center[1] - width / 2, center[2]),
    ]
    msp.add_polyline3d(points, dxfattribs={'layer': 'Roh', 'color': 198})

    # Kopie des Rechtecks erstellen
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
        schriftgroesse = 9
    elif 160 < length <= 210:
        schriftgroesse = 11
    else:
        schriftgroesse = 14

    # Text mit den angegebenen Seitenlängen und Höhe hinzufügen
    text = f"X: {length} mm\n Y: {width} mm\n Z: {height} mm"
    text = msp.add_text(text, dxfattribs={'height': schriftgroesse, 'layer': 'Roh', 'color': 90})

    x, y = (-length / 2), (width / 2) + 4
    text.dxf.insert = (x, y, height - 4)
    text.dxf.rotation = 0

    file_path = r"K:\Esprit\NC-Files\AT-25-KW23\Hasanovic\3.MI\!rohteil.dxf"

    try:
        doc.saveas(file_path)
        print(f"DXF '{file_path}' wurde gespeichert.")
    except IOError as e:
        print(f"Fehler beim Speichern der DXF-Datei unter '{file_path}': {e}")
        print("Stellen Sie sicher, dass der Pfad existiert und Sie Schreibrechte haben.")
        try:
            local_fallback_path = "!rohteil_lokal.dxf"
            doc.saveas(local_fallback_path)
            print(f"DXF wurde stattdessen lokal als '{local_fallback_path}' gespeichert.")
        except Exception as e_local:
            print(f"Fehler auch beim lokalen Speichern: {e_local}")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist beim Speichern aufgetreten: {e}")


if __name__ == "__main__":
    rechteck_erstellen(length=100, width=100, height=100)

