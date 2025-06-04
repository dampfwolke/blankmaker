import ezdxf
from ezdxf import enums  # Für Alignment-Konstanten

def kreis_erstellen(diameter, height, base_offset_factor=0.2):
    """
    Erstellt Kreise und zwei nebeneinander angeordnete, vertikal stehende Texte.
    Die Anordnung der Texte ("Höhe" links, "Durchmesser" rechts) basiert auf dem
    zuletzt bereitgestellten Screenshot.

    diameter: Durchmesser des Kreises in mm
    height: Höhe in mm (Z-Wert des oberen Kreises und der Textebene)
    base_offset_factor: Faktor des Radius, der als Mindestabstand zwischen Kreisrand
                        und dem ersten Textblock genommen wird.
    """
    doc = ezdxf.new("R2010")
    msp = doc.modelspace()

    radius = diameter / 2
    z_offset_unten = -6      # Z-Position des unteren Kreises
    z_text_ebene = height    # Z-Position des oberen Kreises und auch die Z-Ebene der Texte

    # Kreise zeichnen
    msp.add_circle((0, 0, z_offset_unten), radius, dxfattribs={'layer': 'Roh', 'color': 198})
    msp.add_circle((0, 0, z_text_ebene), radius, dxfattribs={'layer': 'Roh', 'color': 198})

    # Dynamische Textgröße (Höhe der einzelnen Zeichen)
    text_char_height = max(1.2, min(diameter * 0.05, 8))

    # --- Platzierungslogik für NEBENEINANDER angeordnete Texte ---
    # Gemäß dem Screenshot (Höhe links, DM rechts, beide 270° rotiert, vertikal zueinander zentriert)

    rotation_grad = 270

    # Die "effektive Breite" eines um 270° rotierten Textblocks auf der Zeichnung
    # (seine Ausdehnung entlang der X-Achse der Zeichnung) ist die ursprüngliche Zeichenhöhe.
    text_block_effective_x_width = text_char_height

    # Abstand vom rechten Kreisrand zum linken Rand des ersten Textblocks ("Höhe")
    gap_circle_to_first_text_edge = max(text_char_height * 0.5, radius * base_offset_factor)

    # Horizontaler Abstand zwischen den beiden Textblöcken
    # (d.h. zwischen dem rechten Rand des "Höhe"-Textes und dem linken Rand des "DM"-Textes)
    # Passen Sie den Faktor (z.B. 0.5, 1.0, 1.5) an, um den Abstand zu justieren.
    horizontal_gap_between_text_blocks = text_char_height * 1.0

    # X-Position des Einfügepunkts für den "Höhe"-Text (linker Text)
    # Der Einfügepunkt (insert) ist die geometrische Mitte des Textblocks.
    x_insert_hoehe = radius + gap_circle_to_first_text_edge + (text_block_effective_x_width / 2)

    # X-Position des Einfügepunkts für den "DM"-Text (rechter Text)
    # Aufbau: X_Höhe_Mitte + halbe_Breite_Höhe_Text + Abstand + halbe_Breite_DM_Text
    x_insert_dm = x_insert_hoehe + (text_block_effective_x_width / 2) + \
                  horizontal_gap_between_text_blocks + \
                  (text_block_effective_x_width / 2)
    # Vereinfacht, da text_block_effective_x_width für beide gleich ist:
    # x_insert_dm = x_insert_hoehe + text_block_effective_x_width + horizontal_gap_between_text_blocks

    # Y-Position der Einfügepunkte.
    # Da halign=CENTER bei Rotation 270° den Text vertikal um den Einfügepunkt zentriert
    # (entlang seiner gerenderten Länge), und die Texte auf gleicher "visueller Höhe"
    # erscheinen sollen (ihre horizontalen Mittellinien auf einer Linie),
    # müssen die Y-Koordinaten der Einfügepunkte gleich sein.
    # Wir zentrieren sie um die Y=0 Achse der Zeichnung.
    y_insert_common = 0.0

    common_text_attribs = {
        'layer': 'Roh',
        'color': 3,  # Grün
        'height': text_char_height, # Dies ist die DXF-Texthöhe (Höhe der einzelnen Zeichen)
        'rotation': rotation_grad,
        # Textausrichtung relativ zum Einfügepunkt (insert):
        # Bei Rotation = 270° und Einfügepunkt = Geometrische Mitte des Textblocks:
        # - halign=CENTER: Der Einfügepunkt ist vertikal in der Mitte des rotierten Textblocks
        #                  (d.h. mittig zur gerenderten "Länge" des Textes entlang Y').
        # - valign=MIDDLE: Der Einfügepunkt ist horizontal in der Mitte des rotierten Textblocks
        #                  (d.h. mittig zur "effektiven Breite" entlang X', die text_char_height ist).
        'halign': enums.TextHAlign.CENTER,
        'valign': enums.TextVAlign.MIDDLE
    }

    # Text 1: Höhe (wird links platziert)
    hoehe_text_str = f"Höhe = {height} mm"
    hoehe_text_insert_point = (x_insert_hoehe, y_insert_common, z_text_ebene)
    msp.add_text(
        hoehe_text_str,
        dxfattribs=common_text_attribs
    ).set_placement(hoehe_text_insert_point)

    # Text 2: Durchmesser (wird rechts platziert)
    dm_text_str = f"Ø DM = {diameter} mm"
    dm_text_insert_point = (x_insert_dm, y_insert_common, z_text_ebene)
    msp.add_text(
        dm_text_str,
        dxfattribs=common_text_attribs
    ).set_placement(dm_text_insert_point)
    # --- Ende Platzierungslogik für nebeneinander ---

    # DXF speichern
    file_path = r"K:\Esprit\NC-Files\AT-25-KW23\Hasanovic\3.MI\!rohteil.dxf"
    # Für lokale Tests können Sie einen einfacheren Pfad verwenden:
    # file_path = "!rohteil_nebeneinander_final.dxf"
    try:
        doc.saveas(file_path)
        print(f"DXF '{file_path}' wurde gespeichert (Layout: Texte nebeneinander).")
    except IOError as e:
        print(f"Fehler beim Speichern der DXF-Datei unter '{file_path}': {e}")
        print("Stellen Sie sicher, dass der Pfad existiert und Sie Schreibrechte haben.")
        try:
            local_fallback_path = "!rohteil_nebeneinander_final_lokal.dxf"
            doc.saveas(local_fallback_path)
            print(f"DXF wurde stattdessen lokal als '{local_fallback_path}' gespeichert.")
        except Exception as e_local:
            print(f"Fehler auch beim lokalen Speichern: {e_local}")
    except Exception as e: # Andere mögliche Fehler (z.B. von ezdxf)
        print(f"Ein unerwarteter Fehler ist beim Speichern aufgetreten: {e}")


if __name__ == "__main__":
    kreis_erstellen(diameter=80, height=20)
    # kreis_erstellen(diameter=60, height=30)
    # kreis_erstellen(diameter=12, height=50, base_offset_factor=0.5)
    # kreis_erstellen(diameter=5, height=10, base_offset_factor=0.8)