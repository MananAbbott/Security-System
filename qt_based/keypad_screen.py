from PyQt6.QtWidgets import QGridLayout, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from base_screen import BaseScreen
from keypad_auth import KeypadAuth

class KeypadScreen(BaseScreen):
    def __init__(self, stacked_widget):
        super().__init__(stacked_widget)

        self.authenticator = KeypadAuth(b'$2b$12$nqliEyVR64cfjerMAKmefe4BeGmFPU0gDzGB2UVcF6czrmGrt0rMK')
        
        self.input_field = QLineEdit(self)
        self.input_field.setFixedSize(300, 50)
        self.input_field.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_field.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.input_field)

        keypad_layout = QGridLayout()
        self.layout.addLayout(keypad_layout)

        buttons = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            'Clear', '0', 'Enter'
        ]

        positions = [(i, j) for i in range(4) for j in range(3)]

        for position, button in zip(positions, buttons):
            if button == 'Clear':
                btn = QPushButton(button, self)
                btn.clicked.connect(self.clear_input)
            elif button == 'Enter':
                btn = QPushButton(button, self)
                btn.clicked.connect(self.submit_input)
            else:
                btn = QPushButton(button, self)
                btn.clicked.connect(lambda _, digit=button: self.on_button_press(digit))

            btn.setFixedSize(100, 80)
            btn.setFont(QFont('Arial', 20))
            
            keypad_layout.addWidget(btn, *position)

    def on_button_press(self, digit):
        self.input_field.setText(self.input_field.text() + digit)

    def clear_input(self):
        self.input_field.clear()

    def submit_input(self):
        entered_code = self.input_field.text()
        if self.authenticator.verify_password(entered_code):
            self.stacked_widget.setCurrentIndex(6)  # Assuming success screen is at index 6
        else:
            QMessageBox.warning(self, "Access Denied", "Incorrect password.")
        self.clear_input()