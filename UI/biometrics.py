import cv2
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from base_screen import BaseScreen

class BiometricsScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        go_back = self.build_button(text="Home", x = 0.07, y = 0.84, on_press=self.return_home)
        go_back.size_hint = (0.1, 0.05)
        self.add_widget(go_back)


    def update_camera(self, dt):
        # Capture frame from camera
        ret, frame = self.capture.read()

        if ret:
            # Convert the frame to texture
            buf = cv2.flip(cv2.flip(frame, 0), 1).tostring()
            image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')

            # Display the image on the widget
            self.camera_image.texture = image_texture

    def on_leave(self, *args):
        # Stop the camera when leaving the screen
        Clock.unschedule(self.update_camera)
        self.capture.release()

    def on_enter(self, *args):
        # Ensure the theme is correct when entering the screen
        super().on_enter(*args)

        # Camera feed widget
        self.camera_image = Image(size_hint=(0.8, 0.6), pos_hint={"center_x": 0.5, "center_y": 0.45})

        # Add the camera image widget to the screen
        self.add_widget(self.camera_image)

        # Initialize the camera and schedule the update
        self.capture = cv2.VideoCapture(0)

        # Restart the camera feed
        if not self.capture.isOpened():
            self.capture.open(0)
        Clock.schedule_interval(self.update_camera, 1.0 / 30.0)  # 30 FPS

