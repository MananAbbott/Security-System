from kivy.clock import Clock
from base_screen import BaseScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

class RFIDScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Label to prompt the user for NFC tap
        self.prompt_label = MDLabel(
            text="Please tap your RFID card to login",
            halign="center",
            font_style="Display",
            font_size=20,
            size_hint=(1, 0.2),
            theme_text_color="Primary",
            pos_hint={"center_x": 0.5, "center_y": 0.6}  # Position the label on the screen
        )
        
        # Button to return to the home screen
        go_back = self.build_button(text="Home", x = 0.07, y = 0.84, on_press=self.return_home)
        go_back.size_hint = (0.1, 0.05)
        self.add_widget(go_back)
        
        # Arrange all elements in a vertical box layout
        main_layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        main_layout.add_widget(self.prompt_label)
        
        self.add_widget(main_layout)
    
    def on_enter(self, *args):
        # This method is called when the screen is entered
        # Here you can initialize or start NFC reading
        self.update_theme_colors()
        print("Waiting for NFC tap...")
        self.prompt_label.text = "Hello Guest! Please tap your RFID card to login"
        # Simulate RFID detection process for now
        Clock.schedule_once(self.mock_rfid_tap, 3)  # Mock NFC tap after 3 seconds
    
    def mock_rfid_tap(self, dt):
        # This method simulates the RFID tap
        print("RFID card tapped! Logging in...")
        self.prompt_label.text = "RFID card detected, logging in..."

        # Add more logic here for what happens after RFID is detected
        # e.g., authenticate the user, transition to another screen, etc.
