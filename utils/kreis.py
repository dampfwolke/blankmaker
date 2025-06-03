import ezdxf

def kreis_erstellen(diameter, height, base_offset=0.35):
    """
    diameter: Durchmesser des Kreises in mm
    height: Höhe in mm
    base_offset: Anteil des Radius, der als Abstand zwischen Kreis und Text genommen wird (z.B. 0.2 = 20%)
    """
    doc = ezdxf.new("R2010")
    msp = doc.modelspace()

    radius = diameter / 2
    z_offset1 = -6
    z_offset2 = height

    # Kreise zeichnen
    msp.add_circle((0, 0, z_offset1), radius, dxfattribs={'layer': 'Roh', 'color': 198})
    msp.add_circle((0, 0, z_offset2), radius, dxfattribs={'layer': 'Roh', 'color': 198})

    # Dynamische Textgröße (mindestens 2.5 mm, maximal 10 mm)
    text_height = max(1.45, min(diameter * 0.05, 8))

    # Abstand zwischen Kreis und Text proportional zum Radius
    dim_offset = radius * base_offset

    # Position für Texte: entlang +X, mit dim_offset Abstand
    x_pos = radius + dim_offset
    y_pos = 0 
    z_pos = z_offset2

    # Rotation 270° -> Text steht senkrecht nach unten
    rotation = 270

    # Text 1: Durchmesser
    diameter_text = msp.add_text(
        f"Ø DM = {diameter} mm",
        dxfattribs={
            'layer': 'Roh',
            'color': 3,
            'height': text_height,
            'rotation': rotation
        }
    )
    diameter_text.dxf.insert = (x_pos, y_pos, z_pos)

    # Abstand zwischen den Texten: 1.5x Texthöhe (dynamisch)
    text_spacing = text_height * 1.3

    # Text 2: Höhe, unter Text 1 (weil Rotation 270° verschiebt sich in X-Richtung)
    height_text = msp.add_text(
        f"Höhe = {height} mm",
        dxfattribs={
            'layer': 'Roh',
            'color': 3,
            'height': text_height,
            'rotation': rotation
        }
    )
    height_text.dxf.insert = (x_pos - text_spacing, y_pos, z_pos)

    # DXF speichern
    doc.saveas("!rohteil.dxf")

if __name__ == "__main__":
    # Test mit verschiedenen Durchmessern
    #kreis_erstellen(15, 25)
    #kreis_erstellen(60, 30)
    kreis_erstellen(12, 50)
