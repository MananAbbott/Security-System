from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QTimer, Qt
from base_screen import BaseScreen

class SuccessScreen(BaseScreen):
    def __init__(self, stacked_widget):
        super().__init__(stacked_widget)
        
        self.welcome_label = QLabel("Welcome", self)
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcome_label.setStyleSheet("font-size: 48px; font-weight: bold;")
        self.layout.addWidget(self.welcome_label)

    def showEvent(self, event):
        super().showEvent(event)
        QTimer.singleShot(5000, self.return_home)  # Return to home screen after 5 seconds