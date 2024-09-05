from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from base_screen import BaseScreen
from kivy.core.window import Window
import subprocess

# HomeScreen inherits from BaseScreen
class HomeScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        label = MDLabel(
            text="Select an authentication method",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.85},
            font_style="Display",
            role="small" 
        )
        
        # Create buttons for the HomeScreen
        detection_button = self.build_button('Biometrics', 0.275, 0.7, self.switch_to_biometrics)
        keypad_button = self.build_button('Keypad', 0.725, 0.7, self.switch_to_keypad)
        NFC_button = self.build_button('RFID', 0.275, 0.45, self.switch_to_rfid)
        guest_button = self.build_button('Guest', 0.725, 0.45, self.switch_to_guest)
        OTP_button = self.build_button('OTP', 0.275, 0.2, self.switch_to_otp)
        sleep_button = self.build_button('Sleep', 0.725, 0.2, self.sleep_screen)
        
        self.add_widget(label)
        self.add_widget(detection_button)
        self.add_widget(keypad_button)
        self.add_widget(NFC_button)
        self.add_widget(guest_button)
        self.add_widget(OTP_button)
        self.add_widget(sleep_button)

    def switch_to_keypad(self, instance, *args):
        app = MDApp.get_running_app()
        app.screen_manager.current = 'keypad'
    
    def switch_to_otp(self, instance, *args):
        app = MDApp.get_running_app()
        app.screen_manager.current = 'otp'
    
    def switch_to_rfid(self, instance, *args):
        app = MDApp.get_running_app()
        app.screen_manager.current = 'rfid'
    
    def switch_to_guest(self, instance, *args):
        app = MDApp.get_running_app()
        app.screen_manager.current = 'guest'

    def switch_to_biometrics(self, instance, *args):
        app = MDApp.get_running_app()
        app.screen_manager.current = 'biometrics'
    
    def sleep_screen(self, instance):
        # Turn off the display (enter sleep mode)
        subprocess.run(['vcgencmd', 'display_power', '0'])

        # Schedule a wake-up listener (tap to wake)
        Clock.schedule_once(self.enable_touch_wake, 0)

    def enable_touch_wake(self, dt):
        # Bind touch to wake the screen
        Window.bind(on_touch_down=self.wake_screen)

    def wake_screen(self, *args):
        # Turn on the display (wake from sleep)
        subprocess.run(['vcgencmd', 'display_power', '1'])

        # Unbind the touch event to prevent multiple calls
        Window.unbind(on_touch_down=self.wake_screen)
        
        # Return to the home screen if needed
        self.return_home(None)