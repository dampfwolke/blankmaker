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
    Ein robuster Event-Handler, der auf Änderungen, Erstellungen und
    Verschiebungen von .esp-Dateien reagiert.
    """

    def __init__(self, backup_destination_path: Path):
        self.backup_destination_path = backup_destination_path
        self.last_event_time = {}
        print(f"Backup-Zielordner ist: {self.backup_destination_path}")

    # --- ZENTRALE LOGIK FÜR ALLE RELEVANTEN EVENTS ---
    def _process_event(self, event):
        """Verarbeitet ein Ereignis, um zu sehen, ob ein Backup erstellt werden soll."""
        # Ignoriere Verzeichnis-Events
        if event.is_directory:
            return

        # Den korrekten Pfad ermitteln: bei 'moved' ist es der Zielpfad
        if event.event_type == 'moved':
            source_path = Path(event.dest_path)
            event_description = f"moved to {source_path.name}"
        else:
            source_path = Path(event.src_path)
            event_description = f"{event.event_type} on {source_path.name}"
        
        # Nur auf .esp-Dateien reagieren
        if source_path.suffix.lower() == '.esp':
            # Verhindern, dass mehrere Events kurz nacheinander Backups auslösen
            now = time.time()
            if now - self.last_event_time.get(source_path, 0) < 2.0:
                print(f"Doppeltes Event für '{source_path.name}' innerhalb von 2s ignoriert.")
                return

            print(f"--> Relevantes Event erkannt: {event_description}")
            self.last_event_time[source_path] = now
            self.create_timestamped_backup(source_path)

    # --- DEBUGGING-METHODE: Zeigt JEDES Event an, das watchdog sieht ---
    def on_any_event(self, event):
        """Loggt jedes einzelne Event für Debugging-Zwecke."""
        # Ignoriere Cache-Dateien von Editoren etc.
        if '.tmp' in str(event.src_path) or '~' in str(event.src_path):
            return
        print(f"[DEBUG] Watchdog-Event: {event}")

    def on_created(self, event):
        """Wird aufgerufen, wenn eine neue Datei im Ordner erstellt wird."""
        self._process_event(event)
        
    def on_modified(self, event):
        """Wird aufgerufen, wenn eine Datei im Ordner geändert wird."""
        self._process_event(event)

    # --- WICHTIGSTE ÄNDERUNG ---
    def on_moved(self, event):
        """Wird aufgerufen, wenn eine Datei umbenannt/verschoben wird."""
        self._process_event(event)

    def create_timestamped_backup(self, source_path: Path):
        """Erstellt eine Sicherungskopie mit Zeitstempel im Dateinamen."""
        try:
            if not source_path.is_file():
                print(f"!! Info: '{source_path.name}' ist keine Datei mehr, Backup übersprungen.")
                return

            self.backup_destination_path.mkdir(parents=True, exist_ok=True)
            timestamp_prefix = datetime.now().strftime("%H%M")
            new_filename = f"{timestamp_prefix}_{source_path.name}"
            destination_path = self.backup_destination_path / new_filename
            
            # Kurze Pause, falls die Datei noch vom Programm gesperrt ist
            time.sleep(0.5)

            shutil.copy2(source_path, destination_path)
            print(f"====> Backup erfolgreich erstellt: {destination_path.name}")

        except FileNotFoundError:
             print(f"!! FEHLER: Quelldatei '{source_path.name}' nicht gefunden beim Kopieren. (War evtl. temporär)")
        except Exception as e:
            print(f"!! FEHLER beim Erstellen des Backups für '{source_path.name}': {e}")


def main():
    """Hauptfunktion: Argumente parsen, Observer starten und in einer Schleife laufen lassen."""
    parser = argparse.ArgumentParser(description="Überwacht einen Ordner auf Änderungen an .esp-Dateien und erstellt Backups.")
    parser.add_argument("--source-folder", type=str, required=True, help="Der zu überwachende Quellordner.")
    parser.add_argument("--backup-folder", type=str, required=True, help="Der Ordner, in dem die Backups gespeichert werden.")
    args = parser.parse_args()

    source_path = Path(args.source_folder)
    backup_path = Path(args.backup_folder)

    if not source_path.is_dir():
        print(f"!! FATALER FEHLER: Der Quellordner '{source_path}' existiert nicht oder ist keine Datei.")
        sys.exit(1)

    print("=" * 40)
    print("Backup-Skript gestartet.")
    print(f"Überwache Ordner: {source_path}")
    print("=" * 40)

    event_handler = EspBackupEventHandler(backup_destination_path=backup_path)
    observer = Observer()
    observer.schedule(event_handler, path=str(source_path), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nBackup-Skript durch Benutzer (Strg+C) beendet.")
    finally:
        observer.stop()
        observer.join()
        print("Observer gestoppt. Programm beendet.")


if __name__ == "__main__":
    main()