from kivymd.uix.button import MDRaisedButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from base_screen import BaseScreen
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from backend.keypad_auth import KeypadAuth
from kivymd.uix.dialog import MDDialog

class KeypadScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        stored_hashed_password = b'$2b$12$nqliEyVR64cfjerMAKmefe4BeGmFPU0gDzGB2UVcF6czrmGrt0rMK' 
        self.authenticator = KeypadAuth(stored_hashed_password)

        self.actual_input = ""
        
        # Display label for showing the input
        self.input_label = MDLabel(
            text="",
            halign="center",
            font_style="H2",
            size_hint=(1, 0.05),
            theme_text_color="Primary",
            bold=True,
        )
        
        # Layout for the keypad
        keypad_layout = MDGridLayout(cols=3, spacing=15, size_hint=(0.4, 0.1), pos_hint={'center_x':0.5 , 'center_y':0.07})
        
        # Buttons for digits 1-9
        for i in range(1, 10):
            button = self.build_button(text=str(i), on_press=self.on_button_press)
            button.font_size = 60
            keypad_layout.add_widget(button)
        
        # Additional buttons for 0, Clear, and Enter
        clear_button = self.build_button(text="Clear", on_press=self.clear_input)
        clear_button.font_size = 60
        zero_button = self.build_button(text="0", on_press=self.on_button_press)
        zero_button.font_size = 60
        enter_button = self.build_button(text="Enter", on_press=self.submit_input)
        enter_button.font_size = 60
        
        keypad_layout.add_widget(clear_button)
        keypad_layout.add_widget(zero_button)
        keypad_layout.add_widget(enter_button)
        
        main_layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20, pos_hint={'center_x':0.5, 'center_y':0.5})
        main_layout.add_widget(self.input_label)
        main_layout.add_widget(keypad_layout)
        
        self.add_widget(main_layout)

        go_back = self.build_button(text="Home", x=0.07, y=0.84, on_press=self.return_home)
        go_back.size_hint = (0.1, 0.05)
        self.add_widget(go_back)

    def on_button_press(self, instance):
        self.actual_input += instance.text
        # Update the label to show asterisks
        self.input_label.text += "*"
    
    def clear_input(self, instance):
        self.input_label.text = ""
        self.actual_input = ""
    
    def submit_input(self, instance):
        entered_code = self.actual_input
        if self.authenticator.verify_password(entered_code):
            self.manager.current = "success"
        else:
            self.show_dialog("Access Denied", "Incorrect password.")
        self.clear_input(None)

    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[MDRaisedButton(text="OK", on_release=lambda x: dialog.dismiss())]
        )
        dialog.open()
