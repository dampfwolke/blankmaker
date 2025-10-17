import pyautogui as pa

from time import sleep

def klicken(x, y, verweilzeit=0.8):
    pa.click(x,y)
    sleep(verweilzeit)

def main():
    # Fokussieren in Esprit Fenster
    klicken(3175, 427)
    # Öffnen
    klicken(1964, 65)
    # Dateiname Cursor klicken
    klicken(2859, 793)
    # Pfad der Esprit Datei reinschreiben
    pa.typewrite("C:\\Users\\hasanovic\\Desktop\\Startmakroesp\\Start.esp")
    # Öffnen klicken
    klicken(3151, 790, 5)
    # Freiklicken
    klicken(2092, 673)
    # Öffnen
    klicken(1964, 65)
    # Dateiname Cursor klicken
    klicken(2859, 793)
    # Pfad der Step Datei reinschreiben
    pa.typewrite("C:\\Users\\hasanovic\\Desktop\\Startmakroesp\\AN.step")
    # Haken bei Verknüpfen setzen
    klicken(2511, 861)
    # Optionen
    klicken(2658, 854)
    # Haken bei Zusammentreffende Oberflächen verbinden
    ###########
    klicken(2815, 632)
    # Ok klicken
    klicken(2954, 755)
    # Öffnen klicken
    klicken(3151, 790, 7)
    # Freiklicken
    klicken(2092, 673)
    # Doppelklick auf Rohlayer
    pa.doubleClick(2033, 733)
    sleep(1)
    # Extras
    klicken(2301, 36)
    # Add-Ins
    klicken(2396, 239)
    # Geladen/entladen
    klicken(2984, 520)
    # OK Klicken
    klicken(3064, 268)
    # Simulationsfenster öffnen
    klicken(2244, 95, 2)
    # Simulationsfenster fokussieren
    klicken(914, 285, 2)
    # Simulationsfenster verschieben Linksklick und halten und loslassen
    pa.dragTo(2257, 160, 1, button='left')
    sleep(2)
    # Simulationsfenster wieder schliessen
    pa.press('Enter')
    sleep(1)
    # Klick auf Konturzug
    klicken(1349, 100)
    # + bei Allgemein aufklappen
    klicken(863, 85)
    # + bei Bearbeitung aufklappen
    klicken(862, 211)
    # + bei Grösse aufklappen
    klicken(862, 409)
    # fokussieren klicken
    klicken(2062, 626)
    # Neue Datei klicken
    klicken(1944, 68)
    # Nein bei Speichernabfrage klicken
    klicken(2883, 568)

if __name__ == "__main__":
    main()
