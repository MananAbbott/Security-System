from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QApplication
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QIcon, QPalette, QColor
import datetime
import os

class BaseScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.layout = QVBoxLayout(self)

        # Set up a timer to update the time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        # Create a horizontal layout for buttons
        self.button_layout = QHBoxLayout()

        self.icon_path = os.path.join(os.path.dirname(__file__), "icons")
        # Create a home button
        self.home_icon_dark = QIcon(os.path.join(self.icon_path, "dark-home.png"))
        self.home_icon_light = QIcon(os.path.join(self.icon_path, "light-home.png"))
        self.home_button = QPushButton(self)
        self.home_button.clicked.connect(self.return_home)
        self.button_layout.addWidget(self.home_button)

        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_layout.addWidget(self.time_label)

        # Create a theme toggle button
        self.light_icon = QIcon(os.path.join(self.icon_path, "light-mode.png"))
        self.dark_icon = QIcon(os.path.join(self.icon_path, "dark-mode.png"))

        self.theme_button = QPushButton(self)
        self.theme_button.clicked.connect(self.toggle_theme)
        self.button_layout.addWidget(self.theme_button)

        # Add the button layout to the main layout
        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

        self.is_dark_theme = False
        self.set_theme()

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%A, %B %d, %Y\n%I:%M:%S %p")
        self.time_label.setText(current_time)

    def return_home(self):
        self.stacked_widget.setCurrentIndex(0)  # Assuming home screen is at index 0

    def toggle_theme(self):
        self.is_dark_theme = not self.is_dark_theme
        self.set_theme()

    def set_theme(self):
        app = QApplication.instance()
        palette = QPalette()

        if self.is_dark_theme:
            # Dark theme
            palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
            palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
            palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
            palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
            palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
            palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
            palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
            palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
            button_border_color = QColor(100, 100, 100)
            self.theme_button.setIcon(self.light_icon) # Replace with actual path
            self.home_button.setIcon(self.home_icon_light)
        else:
            # Light theme
            palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.black)
            palette.setColor(QPalette.ColorRole.Base, QColor(240, 240, 240))
            palette.setColor(QPalette.ColorRole.AlternateBase, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.black)
            palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.black)
            palette.setColor(QPalette.ColorRole.Button, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.black)
            palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
            palette.setColor(QPalette.ColorRole.Link, QColor(0, 0, 255))
            palette.setColor(QPalette.ColorRole.Highlight, QColor(0, 120, 215))
            palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.white)
            button_border_color = QColor(200, 200, 200)
            self.theme_button.setIcon(self.dark_icon)  # Replace with actual path
            self.home_button.setIcon(self.home_icon_dark)

        app.setPalette(palette)
        
        style = f"""
            QPushButton {{
                border: 2px solid {button_border_color.name()};
                border-radius: 5px;
                padding: 5px;
            }}
            QPushButton:hover {{
                background-color: {palette.color(QPalette.ColorRole.Button).lighter(110).name()};
            }}
            QPushButton:pressed {{
                background-color: {palette.color(QPalette.ColorRole.Button).darker(110).name()};
            }}
            QLineEdit {{
                font-size: 30px;
                background-color: {palette.color(QPalette.ColorRole.Base).name()};
                color: {palette.color(QPalette.ColorRole.Text).name()};
                border: 2px solid {button_border_color.name()};
                border-radius: 5px;
                padding: 5px;
                letter-spacing: 8px;
            }}
        """
        app.setStyleSheet(style)

    def build_button(self, text, x, y, on_click):
        button = QPushButton(text, self)
        button.move(x, y)
        button.clicked.connect(on_click)
        return button