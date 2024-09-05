from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from base_screen import BaseScreen


class SuccessScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = MDLabel(
            text="Welcome",
            halign="center",
            font_style="Display",
            font_size=20,
            size_hint=(1, 0.05),
            theme_text_color="Primary",
            bold=True,
        )

        main_layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20, pos_hint={'center_x':0.5, 'center_y':0.5})
        main_layout.add_widget(self.label)
        self.add_widget(main_layout)

        go_back = self.build_button(text="Home", x=0.07, y=0.84, on_press=self.return_home)
        go_back.size_hint = (0.1, 0.05)
        self.add_widget(go_back)
    
    def on_enter(self, *args):
        super().on_enter(*args)
        # wait for 5 seconds then go back to home screen
        Clock.schedule_once(self.return_home, 5)