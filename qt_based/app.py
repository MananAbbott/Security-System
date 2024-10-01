import sys
import os
from PyQt6.QtWidgets import QApplication, QStackedWidget
from PyQt6.QtGui import QFont, QCursor
from PyQt6.QtCore import Qt
from home_screen import HomeScreen
from keypad_screen import KeypadScreen
from otp_screen import OTPScreen
from rfid_screen import RFIDScreen
from guest_screen import GuestScreen
from biometrics_screen import BiometricsScreen
from success_screen import SuccessScreen

# # Try different platform plugins
# platforms = ['windows']
# for platform in platforms:
#     os.environ['QT_QPA_PLATFORM'] = platform
#     print(f"Trying platform: {platform}")
    
#     try:
#         # Enable verbose output for debugging
#         os.environ['QT_DEBUG_PLUGINS'] = '1'
        
class MyApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setFont(QFont('Arial', 10))  # Reduced font size for small screen
        self.stacked_widget = QStackedWidget()

        self.setOverrideCursor(QCursor(Qt.CursorShape.BlankCursor))
        
        # Create and add screens
        self.home_screen = HomeScreen(self.stacked_widget)
        self.keypad_screen = KeypadScreen(self.stacked_widget)
        self.otp_screen = OTPScreen(self.stacked_widget)
        self.rfid_screen = RFIDScreen(self.stacked_widget)
        self.guest_screen = GuestScreen(self.stacked_widget)
        self.biometrics_screen = BiometricsScreen(self.stacked_widget)
        self.success_screen = SuccessScreen(self.stacked_widget)

        self.stacked_widget.addWidget(self.home_screen)
        self.stacked_widget.addWidget(self.keypad_screen)
        self.stacked_widget.addWidget(self.otp_screen)
        self.stacked_widget.addWidget(self.rfid_screen)
        self.stacked_widget.addWidget(self.guest_screen)
        self.stacked_widget.addWidget(self.biometrics_screen)
        self.stacked_widget.addWidget(self.success_screen)

        self.stacked_widget.setFixedSize(320, 480)  # Set size for 3.5" touchscreen
        self.stacked_widget.show()
        self.stacked_widget.showFullScreen()  # Make the application fullscreen

if __name__ == '__main__':
    app = MyApp(sys.argv)
    sys.exit(app.exec())  # Changed from exec_() to exec()

#     except Exception as e:
#         print(f"Failed to initialize with {platform}. Error: {str(e)}")
#     else:
#         print(f"Successfully initialized with {platform}")
#         break
# else:
#     print("Failed to initialize with any platform.")
#     sys.exit(1)