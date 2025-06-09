# scripts/backup.py
import sys
import time
import shutil
from pathlib import Path
from datetime import datetime
import argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class EspBackupEventHandler(FileSystemEventHandler):
    """
    Ein spezieller Event-Handler, der nur auf Änderungen an .esp-Dateien reagiert.
    """

    def __init__(self, backup_destination_path: Path):
        self.backup_destination_path = backup_destination_path
        print(f"Backup-Zielordner ist: {self.backup_destination_path}")

    def on_modified(self, event):
        """Wird aufgerufen, wenn eine Datei im überwachten Ordner geändert wird."""
        # Ignoriere Ereignisse, die sich auf Verzeichnisse beziehen
        if event.is_directory:
            return

        source_path = Path(event.src_path)

        # Prüfe, ob es sich um eine .esp-Datei handelt
        if source_path.suffix.lower() == '.esp':
            print(f"Änderung an .esp-Datei erkannt: {source_path.name}")
            self.create_timestamped_backup(source_path)

    def create_timestamped_backup(self, source_path: Path):
        """Erstellt eine Sicherungskopie mit Zeitstempel im Dateinamen."""
        try:
            # Stelle sicher, dass der Backup-Ordner existiert
            self.backup_destination_path.mkdir(parents=True, exist_ok=True)

            # Erstelle den Zeitstempel-Präfix (Stunde_Minute)
            timestamp_prefix = datetime.now().strftime("%H_%M")

            # Erstelle den neuen Dateinamen und den vollständigen Zielpfad
            new_filename = f"{timestamp_prefix}_{source_path.name}"
            destination_path = self.backup_destination_path / new_filename

            # Kopiere die Datei (copy2 behält Metadaten wie das Änderungsdatum bei)
            shutil.copy2(source_path, destination_path)

            print(f"--> Backup erfolgreich erstellt: {destination_path.name}")

        except Exception as e:
            print(f"!! FEHLER beim Erstellen des Backups für '{source_path.name}': {e}")


def main():
    """Hauptfunktion: Argumente parsen, Observer starten und in einer Schleife laufen lassen."""
    parser = argparse.ArgumentParser(
        description="Überwacht einen Ordner auf Änderungen an .esp-Dateien und erstellt Backups.")
    parser.add_argument("--source-folder", type=str, required=True, help="Der zu überwachende Quellordner.")
    parser.add_argument("--backup-folder", type=str, required=True,
                        help="Der Ordner, in dem die Backups gespeichert werden.")
    args = parser.parse_args()

    source_path = Path(args.source_folder)
    backup_path = Path(args.backup_folder)

    # Prüfen, ob der Quellordner existiert
    if not source_path.is_dir():
        print(f"!! FATALER FEHLER: Der Quellordner '{source_path}' existiert nicht oder ist keine Datei.")
        sys.exit(1)  # Beendet das Skript mit einem Fehlercode

    print("=" * 40)
    print("Backup-Skript gestartet.")
    print(f"Überwache Ordner: {source_path}")
    print("=" * 40)

    # Observer und Event-Handler einrichten
    event_handler = EspBackupEventHandler(backup_destination_path=backup_path)
    observer = Observer()
    # recursive=False, da wir nur den Hauptordner überwachen wollen, nicht die Unterordner
    observer.schedule(event_handler, path=str(source_path), recursive=False)

    observer.start()

    try:
        # Halte das Skript am Leben, während der Observer im Hintergrund arbeitet
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nBackup-Skript durch Benutzer (Strg+C) beendet.")
    finally:
        # Aufräumen, wenn das Skript beendet wird
        observer.stop()
        observer.join()
        print("Observer gestoppt. Programm beendet.")


if __name__ == "__main__":
    main()