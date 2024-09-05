from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon
import datetime

class BaseScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.layout = QVBoxLayout(self)
        
        # Create and set up the time label
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.time_label)

        # Set up a timer to update the time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        # Create a home button
        self.home_button = QPushButton("Home", self)
        self.home_button.clicked.connect(self.return_home)
        self.layout.addWidget(self.home_button)

        # Create a theme toggle button
        self.theme_button = QPushButton(self)
        self.theme_button.setIcon(QIcon("path_to_light_icon.png"))  # Replace with actual path
        self.theme_button.clicked.connect(self.toggle_theme)
        self.layout.addWidget(self.theme_button)

        self.setLayout(self.layout)

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%A, %B %d, %Y | %I:%M:%S %p")
        self.time_label.setText(current_time)

    def return_home(self):
        self.stacked_widget.setCurrentIndex(0)  # Assuming home screen is at index 0

    def toggle_theme(self):
        # Implement theme toggling logic here
        pass

    def build_button(self, text, x, y, on_click):
        button = QPushButton(text, self)
        button.move(x, y)
        button.clicked.connect(on_click)
        return button