# utils/close_nc_editor.py
import time
from pywinauto import Application
import pygetwindow as gw

def find_and_close_error_windows(window_specs):
    """
    Sucht einmalig nach Fenstern, die den Spezifikationen entsprechen, 
    und versucht, diese mit der Tastenkombination Alt+F4 zu schließen.

    Args:
        window_specs (list): Eine Liste von Dictionaries, die die zu suchenden
                             Fenster und deren Eigenschaften definieren.

    Returns:
        bool: True, wenn ein Fenster gefunden und eine Aktion ausgeführt wurde, sonst False.
    """

    ### argument hardcodiert, falls später andere Fenster gebraucht werden löschen und als argument in der funktion aufrufen! ###

    window_specs = [
    {
        'title': 'ESPRIT NC-Editor',
        'max_width': 950, 'min_width': 850,
        'max_height': 850, 'min_height': 750
    },]

    found_and_acted = False
    for spec in window_specs:
        try:
            # Finde alle Fenster, die dem Titel entsprechen
            windows = gw.getWindowsWithTitle(spec['title'])
            if not windows:
                continue

            for window in windows:
                # Prüfe die Größe des Fensters
                size_ok = (spec.get('min_width', 0) <= window.width <= spec.get('max_width', 9999) and
                           spec.get('min_height', 0) <= window.height <= spec.get('max_height', 9999))

                if not size_ok:
                    continue

                # Größe passt, jetzt mit pywinauto verbinden, um den Text zu lesen
                app = Application(backend='uia').connect(handle=window._hWnd, timeout=2)
                win_dialog = app.window(handle=window._hWnd)

                # Prüfe den Textinhalt (falls einer definiert ist)
                text_ok = False
                if 'text_contains' in spec:
                    all_texts = " ".join([w.window_text() for w in win_dialog.children() if w.is_visible()])
                    if spec['text_contains'].lower() in all_texts.lower():
                        text_ok = True
                else:
                    text_ok = True  # Wenn kein Text definiert ist, gilt die Prüfung als erfolgreich

                # Wenn Größe und Text passen, führe die Aktion aus
                if text_ok:
                    action_key = '%{F4}'  # Tastencode für Alt + F4
                    print(
                        f"[{time.strftime('%H:%M:%S')}] Fenster '{spec['title']}' gefunden. "
                        f"Aktion: Schließen (Alt+F4)"
                    )
                    # Sende die Alt+F4 Tastenkombination
                    win_dialog.type_keys(action_key, with_spaces=True)
                    
                    found_and_acted = True
                    # Kurze Pause, damit das Fenster Zeit hat zu reagieren
                    time.sleep(0.3) 
                    # Breche die innere Schleife ab, da wir das Fenster behandelt haben
                    break
            
            if found_and_acted:
                # Breche die äußere Schleife ab, um pro Aufruf nur ein Fenster zu schließen
                break

        except (gw.PyGetWindowException, Exception):
            # Ignoriere Fehler, die auftreten, wenn ein Fenster verschwindet, während wir es prüfen
            pass
            
    return found_and_acted

if __name__ == '__main__':
    # Dieser Teil wird nur ausgeführt, wenn du dieses Skript direkt startest.
    # Er dient zum Testen der Funktion.
    
    print("Dies ist ein Testlauf für das 'error_closer' Modul.")
    print("Es wird einmalig nach den definierten Fenstern gesucht.")

    # Beispiel-Konfiguration, genau wie in deinem alten Skript
    TEST_WINDOW_SPECS = [
        {
            'title': 'ESPRIT NC-Editor',
            'max_width': 950, 'min_width': 850,
            'max_height': 850, 'min_height': 750
        },

        # ... füge hier bei Bedarf die anderen Dictionaries ein
    ]
    
    # Rufe die Funktion mit der Test-Konfiguration auf
    was_closed = find_and_close_error_windows(TEST_WINDOW_SPECS)
    
    if was_closed:
        print("Ein passendes Fenster wurde gefunden und die Schließen-Aktion wurde ausgeführt.")
    else:
        print("Kein passendes Fenster zum Schließen gefunden.")