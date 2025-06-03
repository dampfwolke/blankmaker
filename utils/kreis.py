import ezdxf
from ezdxf import enums  # Für Alignment-Konstanten


def kreis_erstellen(diameter, height, base_offset_factor=0.35):
    """
    diameter: Durchmesser des Kreises in mm
    height: Höhe in mm
    base_offset_factor: Faktor des Radius, der als Mindestabstand zwischen Kreisrand und Textrand genommen wird (z.B. 0.35 = 35%)
    """
    doc = ezdxf.new("R2010")
    msp = doc.modelspace()

    radius = diameter / 2
    z_offset1 = -6
    z_offset2 = height

    # Kreise zeichnen
    msp.add_circle((0, 0, z_offset1), radius, dxfattribs={'layer': 'Roh', 'color': 198})
    msp.add_circle((0, 0, z_offset2), radius, dxfattribs={'layer': 'Roh', 'color': 198})

    # Dynamische Textgröße (mindestens 1.45 mm, maximal 8 mm)
    # Kleinere Mindestgröße kann bei sehr kleinen Durchmessern sinnvoll sein
    text_height = max(1.45, min(diameter * 0.05, 8))

    # Abstand zwischen Kreisaußenkante und Textaußenkante
    # (proportional zum Radius, aber mindestens halbe Texthöhe, um Überlappung bei kleinen Radien zu vermeiden)
    min_gap = text_height * 0.5  # Mindestens halbe Texthöhe als Abstand
    text_gap_from_circle = max(min_gap, radius * base_offset_factor)

    # Nach 270° Rotation ist die "Breite" des Textblocks ungefähr seine ursprüngliche Höhe
    text_block_effective_width = text_height

    # X-Position für die Mitte der vertikalen Textspalte
    # Kreisrand (radius) + gewünschter Spalt + halbe Textblockbreite
    x_center_for_texts = radius + text_gap_from_circle + (text_block_effective_width / 2)

    # Y-Positionen für die Texte, damit sie übereinander gestapelt und um y=0 zentriert sind
    # Abstand zwischen den Mittelpunkten der beiden Textzeilen
    vertical_spacing_between_text_centers = text_height * 1.5  # Etwas mehr Platz als vorher

    y_pos_diameter_text = vertical_spacing_between_text_centers / 2
    y_pos_height_text = -vertical_spacing_between_text_centers / 2

    z_pos = z_offset2  # Beide Texte auf der Höhe des oberen Kreises

    # Rotation 270° -> Text steht senkrecht, von oben nach unten lesbar
    rotation = 270

    common_text_attribs = {
        'layer': 'Roh',
        'color': 3,
        'height': text_height,
        'rotation': rotation,
        # WICHTIG: Textausrichtung relativ zum Einfügepunkt (insert)
        # halign wirkt vor Rotation horizontal, valign vertikal
        # Nach Rotation 270°:
        # - CENTER (halign) sorgt dafür, dass der Textblock vertikal mittig zum insert-Punkt ist.
        # - MIDDLE (valign) sorgt dafür, dass der Textblock horizontal mittig zum insert-Punkt ist.
        'halign': enums.TextHAlign.CENTER,  # Horizontal zentrieren (wird vertikal nach Rotation)
        'valign': enums.TextVAlign.MIDDLE  # Vertikal mittig (wird horizontal nach Rotation)
    }

    # Text 1: Durchmesser
    # Der Einfügepunkt ist jetzt die Mitte des Textes
    diameter_text_insert_point = (x_center_for_texts, y_pos_diameter_text, z_pos)
    msp.add_text(
        f"Ø DM = {diameter} mm",
        dxfattribs=common_text_attribs
    ).set_placement(diameter_text_insert_point)  # set_placement ist flexibler

    # Text 2: Höhe
    # Der Einfügepunkt ist jetzt die Mitte des Textes
    height_text_insert_point = (x_center_for_texts, y_pos_height_text, z_pos)
    msp.add_text(
        f"Höhe = {height} mm",
        dxfattribs=common_text_attribs
    ).set_placement(height_text_insert_point)

    # DXF speichern
    doc.saveas("!rohteil_korrigiert.dxf")
    print("DXF '!rohteil_korrigiert.dxf' wurde gespeichert.")


if __name__ == "__main__":
    # Test mit verschiedenen Durchmessern
    kreis_erstellen(diameter=15, height=25)
    # kreis_erstellen(diameter=60, height=30)
    # kreis_erstellen(diameter=12, height=50, base_offset_factor=0.5) # Test mit kleinerem Kreis
    # kreis_erstellen(diameter=5, height=10, base_offset_factor=0.8) # Test mit sehr kleinem Kreis
