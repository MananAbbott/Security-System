# Import libraries
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from keypad import KeypadScreen
from home_screen import HomeScreen
from otp import otpScreen
from rfid import RFIDScreen
from guest import guestScreen
from biometrics import BiometricsScreen

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Set the initial theme to Dark
        self.screen_manager = MDScreenManager()
        self.screen_manager.add_widget(HomeScreen(name="home"))
        self.screen_manager.add_widget(KeypadScreen(name="keypad"))
        self.screen_manager.add_widget(otpScreen(name="otp"))
        self.screen_manager.add_widget(RFIDScreen(name="rfid"))
        self.screen_manager.add_widget(guestScreen(name="guest"))
        self.screen_manager.add_widget(BiometricsScreen(name="biometrics"))
        return self.screen_manager

# Run the application
MyApp().run()
