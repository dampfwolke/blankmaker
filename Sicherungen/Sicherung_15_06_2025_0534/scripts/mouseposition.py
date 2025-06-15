import tkinter as tk
from tkinter import scrolledtext, messagebox
import pyautogui # Für globale Mausposition (kann bleiben, aber pynput gibt auch Pos)
import keyboard  # Für globale Hotkeys
import time
import threading # Um Listener nicht-blockierend zu machen
import queue     # Für Thread-sichere Kommunikation
from pynput import mouse # NEU: Für globale Maus-Hooks

# --- Konfiguration ---
SHORTCUT_KEY = "f12"
UPDATE_DELAY_MS = 50
# ---------------------

class MouseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mauspositions-Tracker (Global Klick)")
        self.root.minsize(350, 250)

        # Zustand für Bereichsmessung
        self.is_measuring = False
        self.start_point = None
        self.end_point = None
        self.mouse_listener = None # NEU: Variable für den pynput Listener

        # Queue für die Kommunikation von Listener-Threads zum Tkinter-Thread
        self.event_queue = queue.Queue()

        # --- GUI Elemente ---
        self.info_frame = tk.Frame(root)
        self.info_frame.pack(pady=5, padx=10, fill=tk.X)

        self.pos_label = tk.Label(self.info_frame, text="Mausposition: X=????, Y=????")
        self.pos_label.pack(side=tk.LEFT, expand=True)

        self.mode_label = tk.Label(self.info_frame, text="Modus: Normal", fg="blue")
        self.mode_label.pack(side=tk.RIGHT)

        self.measure_button = tk.Button(root, text="Bereichsmessung starten (Global)", command=self.toggle_measure_mode)
        self.measure_button.pack(pady=5, padx=10, fill=tk.X)

        self.output_text = scrolledtext.ScrolledText(root, height=10, width=50, wrap=tk.WORD)
        self.output_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.output_text.configure(state='disabled')

        # --- Initialisierung ---
        self.update_mouse_pos_display()
        self.setup_global_hooks() # Keyboard Hook
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.check_queue()

        self.log_output(f"Tracker gestartet. Drücke '{SHORTCUT_KEY.upper()}', um die aktuelle Mausposition zu loggen.")
        self.log_output("Klicke auf 'Bereichsmessung starten', um den globalen Messmodus zu aktivieren.")
        self.log_output("WARNUNG: Globale Maus-Hooks benötigen ggf. Admin/System-Berechtigungen.")

    def log_output(self, message):
        """Fügt eine Nachricht zum Ausgabefenster hinzu."""
        self.output_text.configure(state='normal')
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.see(tk.END)
        self.output_text.configure(state='disabled')

    def update_mouse_pos_display(self):
        """Aktualisiert die Anzeige der aktuellen Mausposition."""
        try:
            # Behalte pyautogui hierfür, es ist einfach und direkt
            x, y = pyautogui.position()
            self.pos_label.config(text=f"Mausposition: X={x}, Y={y}")
        except Exception as e:
            self.pos_label.config(text="Mausposition: Fehler")
            # print(f"Fehler beim Abrufen der Mausposition: {e}") # Weniger störend
        finally:
            self.root.after(UPDATE_DELAY_MS, self.update_mouse_pos_display)

    def capture_position_hook(self):
        """Keyboard Hook Callback -> Queue"""
        try:
            pos = pyautogui.position()
            self.event_queue.put(("shortcut_pressed", pos))
        except Exception as e:
            print(f"Fehler im Shortcut-Hook: {e}")
            self.event_queue.put(("error", f"Fehler im Shortcut-Hook: {e}"))

    # --- NEU: pynput Maus Listener Callbacks ---
    def on_global_click(self, x, y, button, pressed):
        """Callback für den globalen pynput Maus-Listener."""
        # Nur auf Linksklick reagieren, nur wenn Taste gedrückt wird (nicht losgelassen)
        # UND nur wenn wir im Messmodus sind!
        if self.is_measuring and button == mouse.Button.left and pressed:
            # Sende Klick-Event an den Hauptthread über die Queue
            self.event_queue.put(("measure_click", (x, y)))
            # WICHTIG: Keine GUI-Updates direkt hier machen!

    def start_mouse_listener(self):
        """Startet den globalen Maus-Listener in einem separaten Thread."""
        if self.mouse_listener is None:
            try:
                # Erstelle den Listener, non-blocking
                self.mouse_listener = mouse.Listener(on_click=self.on_global_click)
                # Starte den Listener in seinem eigenen Thread
                self.mouse_listener.start()
                self.log_output("Globaler Maus-Listener für Messung gestartet.")
                print("pynput Maus-Listener gestartet.")
            except Exception as e:
                 self.log_output(f"[FEHLER] Maus-Listener konnte nicht gestartet werden: {e}")
                 print(f"Fehler beim Starten des pynput Maus-Listeners: {e}")
                 messagebox.showerror("Listener Fehler", f"Konnte globalen Maus-Listener nicht starten.\n\n{e}\n\nPrüfe Berechtigungen (Admin/Bedienungshilfen).")
                 # Messmodus direkt wieder beenden, da Listener nicht läuft
                 self.stop_mouse_listener() # Stellt sicher, dass ggf. Reste gestoppt werden
                 self.is_measuring = False # Zustand korrigieren
                 self.update_gui_for_mode() # GUI zurücksetzen


    def stop_mouse_listener(self):
        """Stoppt den globalen Maus-Listener."""
        if self.mouse_listener:
            try:
                self.mouse_listener.stop()
                # Warten bis der Thread wirklich beendet ist (optional, aber sauberer)
                # self.mouse_listener.join() # Kann manchmal blockieren, wenn nicht sauber gestoppt
                self.mouse_listener = None
                self.log_output("Globaler Maus-Listener für Messung gestoppt.")
                print("pynput Maus-Listener gestoppt.")
            except Exception as e:
                 self.log_output(f"[FEHLER] Maus-Listener konnte nicht gestoppt werden: {e}")
                 print(f"Fehler beim Stoppen des pynput Maus-Listeners: {e}")

    # --- Modifizierte Methoden ---

    def check_queue(self):
        """Überprüft die Queue auf Ereignisse von den Listener-Threads."""
        try:
            while True:
                event_type, data = self.event_queue.get_nowait()

                if event_type == "shortcut_pressed":
                    x, y = data
                    self.log_output(f"[{time.strftime('%H:%M:%S')}] Position erfasst ({SHORTCUT_KEY.upper()}): X={x}, Y={y}")
                elif event_type == "measure_click": # NEU: Event vom Maus-Listener
                    if self.is_measuring: # Doppelte Sicherheitsprüfung
                         x, y = data
                         self.process_measure_click(x, y) # Verarbeitung im Hauptthread
                elif event_type == "error":
                     self.log_output(f"[FEHLER] {data}")

        except queue.Empty:
            pass # Nichts in der Queue
        finally:
            self.root.after(100, self.check_queue)

    def setup_global_hooks(self):
        """Richtet den globalen Keyboard-Listener ein."""
        try:
            keyboard.add_hotkey(SHORTCUT_KEY, self.capture_position_hook)
            print(f"Globaler Keyboard-Hotkey '{SHORTCUT_KEY}' registriert.")
        except Exception as e:
            self.log_output(f"[FEHLER] Keyboard-Hotkey konnte nicht registriert werden: {e}")
            print(f"Fehler beim Registrieren des Keyboard-Hotkeys: {e}")
            messagebox.showerror("Hotkey Fehler", f"Konnte globalen Keyboard-Hotkey '{SHORTCUT_KEY}' nicht registrieren.\n\n{e}\n\nPrüfe Berechtigungen.")

    def update_gui_for_mode(self):
        """Aktualisiert Button-Text und Modus-Label basierend auf dem Zustand."""
        if self.is_measuring:
            if self.start_point is None:
                self.measure_button.config(text="Bereichsmessung stoppen (Klick 1/2)")
                self.mode_label.config(text="Modus: MESSEN (Global - Klick 1)", fg="red")
                self.root.config(cursor="crosshair") # Cursor ändern
            else:
                self.measure_button.config(text="Bereichsmessung stoppen (Klick 2/2)")
                self.mode_label.config(text="Modus: MESSEN (Global - Klick 2)", fg="red")
                self.root.config(cursor="crosshair")
        else:
            self.measure_button.config(text="Bereichsmessung starten (Global)")
            self.mode_label.config(text="Modus: Normal", fg="blue")
            self.start_point = None # Sicherstellen, dass Punkte zurückgesetzt sind
            self.end_point = None
            self.root.config(cursor="") # Standard Cursor


    def toggle_measure_mode(self):
        """Schaltet den globalen Messmodus ein oder aus."""
        if self.is_measuring:
            # Messmodus beenden
            self.is_measuring = False
            self.stop_mouse_listener() # WICHTIG: Listener stoppen
            self.update_gui_for_mode() # GUI aktualisieren
            self.log_output("Bereichsmessung gestoppt.")
        else:
            # Messmodus starten
            self.is_measuring = True
            # Listener starten (macht GUI-Updates bei Erfolg/Misserfolg selbst)
            self.start_mouse_listener()
            # GUI sofort aktualisieren (falls Listener erfolgreich startet)
            if self.mouse_listener: # Nur wenn Start erfolgreich war
                 self.update_gui_for_mode()
                 self.log_output("Bereichsmessung gestartet. Klicke irgendwo auf den Startpunkt (links oben).")


    def process_measure_click(self, click_x, click_y):
        """Verarbeitet einen Klick, der im Messmodus erkannt wurde (wird von check_queue aufgerufen)."""
        if not self.is_measuring:
             return # Sollte nicht passieren, aber sicher ist sicher

        if self.start_point is None:
            # Erster Klick: Startpunkt speichern
            self.start_point = (click_x, click_y)
            self.log_output(f"Startpunkt gesetzt: X={click_x}, Y={click_y}")
            # GUI aktualisieren, um anzuzeigen, dass der nächste Klick erwartet wird
            self.update_gui_for_mode()

        else:
            # Zweiter Klick: Endpunkt speichern, Berechnung durchführen
            self.end_point = (click_x, click_y)
            self.log_output(f"Endpunkt gesetzt: X={click_x}, Y={click_y}")

            start_x, start_y = self.start_point
            end_x, end_y = self.end_point
            width = abs(end_x - start_x)
            height = abs(end_y - start_y)

            output_str = (
                f"--- Bereichsmessung Ergebnis ---\n"
                f"  Startpunkt: ({start_x}, {start_y})\n"
                f"  Endpunkt:   ({end_x}, {end_y})\n"
                f"  Breite:     {width} px\n"
                f"  Höhe:       {height} px\n"
                f"--------------------------------"
            )
            self.log_output(output_str)

            # Punkte zurücksetzen für die nächste Messung (Modus bleibt aktiv)
            self.start_point = None
            self.end_point = None
            self.update_gui_for_mode() # GUI aktualisieren für nächsten "Klick 1"
            self.log_output("Neue Bereichsmessung bereit. Klicke auf den Startpunkt oder stoppe den Modus.")


    def on_closing(self):
        """Aufräumarbeiten beim Schließen des Fensters."""
        print("Schließe Anwendung und entferne Hooks/Listener...")
        # Stoppe den Maus-Listener, falls er läuft
        self.stop_mouse_listener()
        # Entferne Keyboard-Hooks
        try:
            keyboard.remove_all_hotkeys()
            print("Keyboard-Hooks entfernt.")
        except Exception as e:
            print(f"Fehler beim Entfernen der Keyboard-Hooks: {e}")
        self.root.destroy()

# --- Hauptteil ---
if __name__ == "__main__":
    # Wichtiger Hinweis zu pynput/keyboard Berechtigungen
    print("INFO: Dieses Skript verwendet globale Keyboard- und Maus-Hooks.")
    print("INFO: Auf macOS/Linux sind eventuell Admin-Rechte (sudo) oder")
    print("INFO: explizite Berechtigungen in den Systemeinstellungen")
    print("INFO: (z.B. Bedienungshilfen/Input Monitoring) erforderlich.")

    root = tk.Tk()
    app = MouseTrackerApp(root)
    root.mainloop()