from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont


class ConfirmationDialog(QDialog):
    def __init__(self, title: str, text: str, timeout: int = 10, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setModal(True)  # Blockiert andere Fenster der Anwendung

        self.remaining_time = timeout
        self.result_on_timeout = True  # Bei Timeout wird "Ja" angenommen

        # Layouts
        main_layout = QVBoxLayout(self)
        button_layout = QHBoxLayout()

        # Widgets
        self.info_label = QLabel(text)
        self.info_label.setFont(QFont("Arial", 12))

        self.timer_label = QLabel()
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setFont(QFont("Arial", 10, QFont.Bold))

        self.yes_button = QPushButton("Fortfahren (Ja)")
        self.no_button = QPushButton("Überspringen (Nein)")

        # Standard-Button setzen (wird bei Enter ausgelöst)
        self.yes_button.setDefault(True)

        # Layouts füllen
        main_layout.addWidget(self.info_label)
        main_layout.addWidget(self.timer_label)
        main_layout.addLayout(button_layout)

        button_layout.addStretch()
        button_layout.addWidget(self.yes_button)
        button_layout.addWidget(self.no_button)
        button_layout.addStretch()

        # Signale verbinden
        self.yes_button.clicked.connect(self.accept)  # accept() schließt den Dialog und gibt QDialog.Accepted zurück
        self.no_button.clicked.connect(self.reject)  # reject() schließt und gibt QDialog.Rejected zurück

        # Timer einrichten
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # Jede Sekunde
        self.timer.timeout.connect(self.update_countdown)
        self.update_countdown()  # Initialen Text setzen
        self.timer.start()

    def update_countdown(self):
        """ Zählt den Timer runter und aktualisiert das Label. """
        if self.remaining_time > 0:
            self.timer_label.setText(f"Automatische Fortsetzung in {self.remaining_time} Sekunden...")
            self.yes_button.setText(f"Fortfahren (Ja) [{self.remaining_time}]")
            self.remaining_time -= 1
        else:
            self.timer.stop()
            if self.result_on_timeout:
                self.accept()  # Simuliert Klick auf "Ja"
            else:
                self.reject()  # Simuliert Klick auf "Nein"