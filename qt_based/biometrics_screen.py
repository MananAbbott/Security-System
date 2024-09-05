from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
from base_screen import BaseScreen
import cv2

class BiometricsScreen(BaseScreen):
    def __init__(self, stacked_widget):
        super().__init__(stacked_widget)
        
        self.camera_label = QLabel(self)
        self.layout.addWidget(self.camera_label)

        self.capture = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

    def showEvent(self, event):
        super().showEvent(event)
        self.capture = cv2.VideoCapture(0)
        self.timer.start(30)  # Update every 30 ms (approximately 33 fps)

    def hideEvent(self, event):
        super().hideEvent(event)
        if self.capture is not None:
            self.capture.release()
        self.timer.stop()

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            self.camera_label.setPixmap(pixmap)

    # Add biometric authentication logic here
    def authenticate(self):
        # Implement your biometric authentication logic
        # If authentication is successful:
        # self.stacked_widget.setCurrentIndex(6)  # Assuming success screen is at index 6
        pass