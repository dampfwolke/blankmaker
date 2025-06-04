import ezdxf
from ezdxf import enums  # Für Alignment-Konstanten

def kreis_erstellen(diameter, height, base_offset_factor=0.13):
    """
    diameter: Durchmesser des Kreises in mm
    height: Höhe in mm
    base_offset_factor: Faktor des Radius, der als Mindestabstand zwischen Kreisrand und Textrand genommen wird
    """
    doc = ezdxf.new("R2010")
    msp = doc.modelspace()

    radius = diameter / 2
    z_offset1 = -6  # Unterer Kreis
    z_offset2 = height -6 # Oberer Kreis

    # Kreise zeichnen
    msp.add_circle((0, 0, z_offset1), radius, dxfattribs={'layer': 'Roh', 'color': 198})
    msp.add_circle((0, 0, z_offset2), radius, dxfattribs={'layer': 'Roh', 'color': 198})

    # Dynamische Textgröße (mindestens 1.2 mm, maximal 8 mm)
    text_height = max(1.2, min(diameter * 0.05, 8))

    min_gap_circle_text = text_height * 0.5
    text_gap_from_circle_edge = max(min_gap_circle_text, radius * base_offset_factor)
    text_block_effective_width = text_height
    x_center_for_texts = radius + text_gap_from_circle_edge + (text_block_effective_width / 2)

    diameter_text_str = f"Ø DM = {diameter} mm"
    height_text_str = f"Höhe = {height} mm"

    # --- WICHTIGE ANPASSUNG HIER ---
    # Geschätztes Verhältnis von durchschnittlicher Zeichenbreite zu Zeichenhöhe.
    # Für viele CAD-Schriften (SHX) ist ein Wert zwischen 0.5 und 0.7 realistischer als höhere Werte.
    # Passen Sie diesen Wert an, wenn der vertikale Abstand immer noch nicht stimmt.
    font_char_aspect_ratio_approx = 0.12
    
    rendered_length_diameter_text = len(diameter_text_str) * text_height * font_char_aspect_ratio_approx
    rendered_length_height_text = len(height_text_str) * text_height * font_char_aspect_ratio_approx

    # Gewünschter visueller Abstand zwischen der Unterkante des oberen Textes
    # und der Oberkante des unteren Textes.
    # Passen Sie den Faktor (z.B. 0.5, 0.75, 1.0) an, um den Abstand zu justieren.
    desired_gap_between_text_blocks = text_height * 0.5

    vertical_spacing_between_text_centers = \
        (rendered_length_diameter_text / 2) + \
        (rendered_length_height_text / 2) + \
        desired_gap_between_text_blocks

    y_center_diameter_text = vertical_spacing_between_text_centers
    y_center_height_text = -vertical_spacing_between_text_centers

    z_pos = z_offset2
    rotation = 310

    common_text_attribs = {
        'layer': 'Roh',
        'color': 3, # Grün
        'height': text_height,
        'rotation': rotation,
        'halign': enums.TextHAlign.CENTER,
        'valign': enums.TextVAlign.MIDDLE
    }

    diameter_text_insert_point = (x_center_for_texts, y_center_diameter_text, z_pos)
    msp.add_text(
        diameter_text_str,
        dxfattribs=common_text_attribs
    ).set_placement(diameter_text_insert_point)

    height_text_insert_point = (x_center_for_texts, y_center_height_text, z_pos)
    msp.add_text(
        height_text_str,
        dxfattribs=common_text_attribs
    ).set_placement(height_text_insert_point)

    file_path = r"K:\Esprit\NC-Files\AT-25-KW23\Hasanovic\3.MI\!rohteil.dxf"
    # Für lokale Tests: file_path = "!rohteil_korrigiert_final.dxf"
    try:
        doc.saveas(file_path)
        print(f"DXF '{file_path}' wurde gespeichert.")
    except IOError as e:
        print(f"Fehler beim Speichern der DXF-Datei unter '{file_path}': {e}")
        print("Stellen Sie sicher, dass der Pfad existiert und Sie Schreibrechte haben.")
        try:
            local_fallback_path = "!rohteil_korrigiert_final_lokal.dxf"
            doc.saveas(local_fallback_path)
            print(f"DXF wurde stattdessen lokal als '{local_fallback_path}' gespeichert.")
        except Exception as e_local:
            print(f"Fehler auch beim lokalen Speichern: {e_local}")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist beim Speichern aufgetreten: {e}")

if __name__ == "__main__":
    kreis_erstellen(diameter=80, height=20)
    # kreis_erstellen(diameter=60, height=30)
    # kreis_erstellen(diameter=12, height=50, base_offset_factor=0.5) 
    # kreis_erstellen(diameter=5, height=10, base_offset_factor=0.8)