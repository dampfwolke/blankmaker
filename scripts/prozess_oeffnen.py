# scripts/hotkey_script.py
from pathlib import Path
import pynput
import pyautogui
import time
from functools import partial

# --- Konfiguration ---
# Hier können alle Einstellungen einfach geändert werden.
CONFIDENCE_LEVEL = 0.85
CLICK_TIMEOUT_SECONDS = 2.0
IMAGE1_FILENAME = "verk.PNG"
IMAGE2_FILENAME = "erstellen.PNG"
HOTKEY = pynput.keyboard.Key.f12


# --- Hilfsfunktionen ---

def find_and_click_with_timeout(image_path: Path, timeout: float, confidence: float) -> bool:
    """
    Sucht ein Bild auf dem Bildschirm für eine bestimmte Zeit und klickt darauf, wenn es gefunden wird.

    Args:
        image_path: Der Pfad zum Bild, das gesucht werden soll.
        timeout: Die maximale Wartezeit in Sekunden.
        confidence: Die Genauigkeit für die Bilderkennung (0.0 bis 1.0).

    Returns:
        True, wenn das Bild gefunden und geklickt wurde, sonst False.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            position = pyautogui.locateCenterOnScreen(
                str(image_path),  # pyautogui benötigt einen String-Pfad
                confidence=confidence,
                grayscale=True
            )
            if position:
                pyautogui.click(position)
                print(f"Bild '{image_path.name}' bei {position} gefunden und geklickt.")
                return True
        except pyautogui.PyAutoGUIException as e:
            # Dieser Fehler tritt auf, wenn das Bild nicht gefunden wird. Wir ignorieren ihn und versuchen es erneut.
            pass
        time.sleep(0.05)  # Kurze Pause, um die CPU zu schonen

    print(f"Warnung: Bild '{image_path.name}' konnte nach {timeout}s nicht gefunden werden.")
    return False


def perform_hotkey_action(image1_path: Path, image2_path: Path):
    """
    Führt die vollständige Sequenz aus: Rechtsklick, Klick auf Bild 1, Klick auf Bild 2.
    """
    print(f"\n--- F12 gedrückt: Starte Aktion um {time.strftime('%H:%M:%S')} ---")
    pyautogui.rightClick()
    print("Rechtsklick ausgeführt.")
    time.sleep(0.05)  # Kurze Pause nach dem Rechtsklick, damit das Kontextmenü erscheint

    # Versuche, auf das erste Bild zu klicken
    find_and_click_with_timeout(image1_path, CLICK_TIMEOUT_SECONDS, CONFIDENCE_LEVEL)

    # Versuche, auf das zweite Bild zu klicken
    find_and_click_with_timeout(image2_path, CLICK_TIMEOUT_SECONDS, CONFIDENCE_LEVEL)
    print("--- Aktion beendet ---")


# --- Hauptlogik ---

def main():
    """Hauptfunktion: Setzt Pfade auf, definiert den Listener und startet ihn."""

    # 1. Relative Pfade zu den Bildern erstellen
    # Das Skript findet die Bilder immer im Unterordner "images", egal von wo es gestartet wird.
    script_dir = Path(__file__).parent
    image_folder = script_dir / "images"
    image1 = image_folder / IMAGE1_FILENAME
    image2 = image_folder / IMAGE2_FILENAME

    # 2. Prüfen, ob die Bilddateien existieren
    if not image1.is_file() or not image2.is_file():
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"FEHLER: Bilddateien nicht gefunden!")
        print(f"  Erwarteter Pfad für Bild 1: {image1}")
        print(f"  Erwarteter Pfad für Bild 2: {image2}")
        print("  Stelle sicher, dass die Bilder im Ordner 'scripts/images' liegen.")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return  # Skript beenden, wenn Bilder fehlen

    # 3. Den Listener vorbereiten
    # Wir verwenden partial, um die Bildpfade an unsere Action-Funktion zu "binden".
    # Das ist sauberer als globale Variablen zu verwenden.
    action_with_paths = partial(perform_hotkey_action, image1_path=image1, image2_path=image2)

    def on_press(key):
        if key == HOTKEY:
            action_with_paths()

    # 4. Den Listener starten und das Skript am Laufen halten
    print("=" * 40)
    print("Hotkey-Skript für F12-Automatisierung gestartet.")
    print(f"Überwacht die Taste: {HOTKEY}")
    print("Drücke Strg+C in der Konsole, um das Skript manuell zu beenden.")
    print("=" * 40)

    # Der `with`-Block sorgt dafür, dass der Listener ordnungsgemäß läuft und beendet wird.
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nListener durch Benutzer (Strg+C) gestoppt. Beende Skript.")


if __name__ == "__main__":
    main()