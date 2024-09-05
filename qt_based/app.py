import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5.QtGui import QFont
from home_screen import HomeScreen
from keypad_screen import KeypadScreen
from otp_screen import OTPScreen
from rfid_screen import RFIDScreen
from guest_screen import GuestScreen
from biometrics_screen import BiometricsScreen
from success_screen import SuccessScreen

class MyApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setFont(QFont('Arial', 12))
        self.stacked_widget = QStackedWidget()
        
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

        self.stacked_widget.setFixedSize(480, 320)  # Set size for Raspberry Pi 7" touchscreen
        self.stacked_widget.show()

if __name__ == '__main__':
    app = MyApp(sys.argv)
    sys.exit(app.exec_())