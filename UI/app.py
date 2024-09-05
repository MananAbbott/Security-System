# Import libraries
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import NoTransition
from keypad import KeypadScreen
from home_screen import HomeScreen
from otp import otpScreen
from rfid import RFIDScreen
from guest import guestScreen
from biometrics import BiometricsScreen
from success import SuccessScreen


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Set the initial theme to Dark
        self.screen_manager = MDScreenManager(transition=NoTransition())
        self.screen_manager.add_widget(HomeScreen(name="home")) # Ready
        self.screen_manager.add_widget(KeypadScreen(name="keypad")) # Ready
        self.screen_manager.add_widget(otpScreen(name="otp")) # Ready
        self.screen_manager.add_widget(RFIDScreen(name="rfid"))
        self.screen_manager.add_widget(guestScreen(name="guest"))
        self.screen_manager.add_widget(BiometricsScreen(name="biometrics"))
        self.screen_manager.add_widget(SuccessScreen(name="success")) # Ready
        return self.screen_manager

# Run the application with cProfile
MyApp().run()
