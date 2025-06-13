# scripts/error_closer_script.py
import time
from pywinauto import Application
import pygetwindow as gw

# ----------------------------------------
# Konfiguration
# ----------------------------------------
# Hier können alle zu suchenden Fenster und deren Eigenschaften definiert werden.
WINDOW_SPECS = [
    {
        'title': 'esprit',
        'max_width': 450, 'min_width': 380,
        'max_height': 180, 'min_height': 140,
        'text_contains': "NC-PROGRAMM NICHT FÜR 3-ACHS-MASCHINE GEEIGNET",
        'action': '{ENTER}'  # Aktion, die ausgeführt wird (pywinauto-Syntax)
    },
    {
        'title': 'ESPRIT NC-Editor',
        'max_width': 600, 'min_width': 400,
        'max_height': 300, 'min_height': 160,
        'text_contains': "Der Prozess kann nicht auf die Datei",
        'action': '{ENTER}'
    },
    {
        'title': 'Fehler',
        'max_width': 295, 'min_width': 280,
        'max_height': 165, 'min_height': 150,
        'text_contains': "Fehler beim Anlegen des Prozesses",
        'action': '{ENTER}'
    },
    {
        'title': 'Pimpel Milling Utilities',
        'max_width': 210, 'min_width': 190,
        'max_height': 315, 'min_height': 275,
        'text_contains': "Blockgeometrie",
        'action': '{ENTER}'
    },
    # Hier können bei Bedarf weitere Fenster-Spezifikationen hinzugefügt werden.
]

# Zeit in Sekunden zwischen den Suchdurchläufen
SLEEP_TIMER = 0.5


# ----------------------------------------
# Kernlogik
# ----------------------------------------

def check_and_close_windows():
    """Sucht nach den definierten Fenstern und führt die entsprechende Aktion aus."""
    for spec in WINDOW_SPECS:
        try:
            # Finde alle Fenster, die dem Titel entsprechen
            windows = gw.getWindowsWithTitle(spec['title'])
            if not windows:
                continue  # Nächstes Fenster in der Liste prüfen

            for window in windows:
                # Prüfe die Größe des Fensters
                size_ok = (spec['min_width'] <= window.width <= spec['max_width'] and
                           spec['min_height'] <= window.height <= spec['max_height'])

                if not size_ok:
                    continue  # Größe passt nicht, nächstes gefundenes Fenster prüfen

                # Größe passt, jetzt mit pywinauto verbinden, um den Text zu lesen
                app = Application(backend='uia').connect(handle=window._hWnd, timeout=2)
                win_dialog = app.window(handle=window._hWnd)

                # Prüfe den Textinhalt (falls einer definiert ist)
                text_ok = False
                if 'text_contains' in spec:
                    # Sammle allen sichtbaren Text aus dem Dialog
                    all_texts = " ".join([w.window_text() for w in win_dialog.children() if w.is_visible()])
                    if spec['text_contains'].lower() in all_texts.lower():
                        text_ok = True
                else:
                    text_ok = True  # Wenn kein Text definiert ist, gilt die Prüfung als erfolgreich

                # Wenn Größe und Text passen, führe die Aktion aus
                if text_ok:
                    print(
                        f"[{time.strftime('%H:%M:%S')}] Fenster '{spec['title']}' mit passendem Inhalt gefunden. Aktion: {spec['action']}")
                    win_dialog.type_keys(spec['action'], with_spaces=True)
                    # Wir gehen davon aus, dass die Aktion das Fenster schließt,
                    # daher `break`, um nicht weiter nach diesem Typ zu suchen.
                    break

        except (gw.PyGetWindowException, Exception) as e:
            # Ignoriere Fehler, die auftreten, wenn ein Fenster verschwindet, während wir es prüfen
            # print(f"Info: Fehler beim Prüfen des Fensters '{spec.get('title', 'Unbekannt')}': {e}")
            pass


# ----------------------------------------
# Hauptfunktion
# ----------------------------------------

def main():
    """Startet die Endlosschleife zur Überwachung der Fenster."""
    print("=" * 40)
    print("Fehlermeldungs-Skript gestartet.")
    print(f"Überwacht {len(WINDOW_SPECS)} Fenstertypen.")
    print("=" * 40)

    try:
        while True:
            check_and_close_windows()
            time.sleep(SLEEP_TIMER)
    except KeyboardInterrupt:
        print("\nSkript durch Benutzer (Strg+C) beendet.")
    except Exception as e:
        print(f"Ein kritischer Fehler ist im Skript aufgetreten: {e}")


if __name__ == "__main__":
    main()