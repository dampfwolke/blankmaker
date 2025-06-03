import ezdxf
import math

def kreis_erstellen(diameter, height, dim_offset=15):
    doc = ezdxf.new("R2010")
    msp = doc.modelspace()

    # Grundwerte
    radius = diameter / 2
    center = (0, 0)
    z_offset1 = -6
    z_offset2 = height - 0

    # Kreise zeichnen
    msp.add_circle((center[0], center[1], z_offset1), radius, dxfattribs={'layer': 'Roh', 'color': 198})
    msp.add_circle((center[0], center[1], z_offset2), radius, dxfattribs={'layer': 'Roh', 'color': 198})

    # Dynamische Textgröße abhängig vom Durchmesser
    text_height = max(2.5, diameter * 0.1)  # z. B. 5% des Durchmessers, mindestens 2.5 mm

    # Rotation auf 270° (senkrecht nach unten)
    angle_deg = 270

    # Position des Texts berechnen (weiterhin entlang X-Achse vom Mittelpunkt weg)
    dx = radius + dim_offset
    dy = 10
    text_z = z_offset2

    # Text 1: Durchmesser
    diameter_text = msp.add_text(
        f"Ø DM = {diameter} mm",
        dxfattribs={
            'layer': 'Roh',
            'color': 3,
            'height': text_height,
            'rotation': angle_deg
        }
    )
    diameter_text.dxf.insert = (dx, dy, text_z)

    # Text 2: Höhe, deutlich versetzt nach links (weil Rotation 270°, verschiebt sich X-Achse nach unten)
    offset_x = -text_height * 2  # Abstand zwischen den Texten, hier 3x Textgröße nach links
    offset_y = 0

    height_text = msp.add_text(
        f"Höhe = {height} mm",
        dxfattribs={
            'layer': 'Roh',
            'color': 3,
            'height': text_height,
            'rotation': angle_deg
        }
    )
    height_text.dxf.insert = (dx + offset_x, dy + offset_y, text_z)

    # DXF speichern
    doc.saveas("!rohteil.dxf")


if __name__ == "__main__":
    kreis_erstellen(50, 25)
