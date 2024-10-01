from PyQt6.QtWidgets import QLabel, QPushButton, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from base_screen import BaseScreen
import subprocess

class HomeScreen(BaseScreen):
    def __init__(self, stacked_widget):
        super().__init__(stacked_widget)
        
        label = QLabel("Select an authentication method", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFont(QFont("Arial", 12))
        self.layout.addWidget(label)

        grid_layout = QGridLayout()
        self.layout.addLayout(grid_layout)

        buttons = [
            ("Biometrics", self.switch_to_biometrics),
            ("Keypad", self.switch_to_keypad),
            ("RFID", self.switch_to_rfid),
            ("Guest", self.switch_to_guest),
            ("OTP", self.switch_to_otp),
            ("Sleep", self.sleep_screen)
        ]

        for i, (text, func) in enumerate(buttons):
            button = QPushButton(text, self)
            button.setMinimumSize(150, 120)
            button.setFont(QFont("Arial", 14))
            button.clicked.connect(func)
            grid_layout.addWidget(button, i // 2, i % 2)
        
        grid_layout.SizeConstraint.SetFixedSize

    def switch_to_biometrics(self):
        self.stacked_widget.setCurrentIndex(5)  # Adjust index as needed

    def switch_to_keypad(self):
        self.stacked_widget.setCurrentIndex(1)  # Adjust index as needed

    def switch_to_rfid(self):
        self.stacked_widget.setCurrentIndex(3)  # Adjust index as needed

    def switch_to_guest(self):
        self.stacked_widget.setCurrentIndex(4)  # Adjust index as needed

    def switch_to_otp(self):
        self.stacked_widget.setCurrentIndex(2)  # Adjust index as needed

    def sleep_screen(self):
        # Turn off the display (enter sleep mode)
        exit()