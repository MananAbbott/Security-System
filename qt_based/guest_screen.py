from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer, Qt
from base_screen import BaseScreen

class GuestScreen(BaseScreen):
    def __init__(self, stacked_widget):
        super().__init__(stacked_widget)
        
        self.prompt_label = QLabel("Hello Guest! Please tap your RFID card to login", self)
        self.prompt_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.prompt_label)

    def showEvent(self, event):
        super().showEvent(event)
        print("Waiting for RFID tap...")
        self.prompt_label.setText("Hello Guest! Please tap your RFID card to login")
        QTimer.singleShot(3000, self.mock_rfid_tap)  # Simulate RFID tap after 3 seconds

    def mock_rfid_tap(self):
        print("RFID card tapped! Logging in...")
        self.prompt_label.setText("RFID card detected, logging in...")
        # Add guest authentication logic here
        # If successful, switch to success screen:
        # self.stacked_widget.setCurrentIndex(6)  # Assuming success screen is at index 6