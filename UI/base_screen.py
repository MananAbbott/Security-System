from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDButton, MDIconButton, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.anchorlayout import AnchorLayout
from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarTitle
from kivy.clock import Clock
from datetime import datetime
from kivymd.uix.gridlayout import MDGridLayout

# BaseScreen class with common elements
class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.theme_buttons = []

        # Toolbar
        self.toolbar = MDTopAppBar(
            pos_hint={"top": 1},
            md_bg_color=self.get_button_color()[2],
            # text_color=self.get_button_color()[1],
        )
        self.toolbar.add_widget(MDTopAppBarTitle(text="", text_color = self.get_button_color()[1]))
        self.add_widget(self.toolbar)

        # Start updating time on the toolbar
        Clock.schedule_interval(self.update_time, 1)

        # Theme Switch Icon Button
        self.theme_icon = MDIconButton(
            icon="weather-night",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_release=self.toggle_theme
        )

        # Bottom layout for theme switch button
        theme_icon_layout = MDBoxLayout(
            orientation="horizontal",
            spacing="10dp",
            size_hint=(None, None),
            height="48dp"
        )
        theme_icon_layout.add_widget(self.theme_icon)

        theme_icon_anchor = AnchorLayout(
            anchor_x='right',
            anchor_y='bottom',
            size_hint=(1, 0.15)
        )
        theme_icon_anchor.add_widget(theme_icon_layout)

        # Add the theme switch button to the screen
        self.add_widget(theme_icon_anchor)

        # Call update_theme_colors to ensure everything is correctly colored initially
        self.update_theme_colors()

    def get_button_color(self):
        app = MDApp.get_running_app()
        if app.theme_cls.theme_style == "Light":
            return [(0.83, 0.83, 0.83, 1), (0, 0, 0, 1), (1, 1, 1, 1)] # grey border, black text, white bg
        else:
            return [(0.83, 0.83, 0.83, 1), (1, 1, 1, 1), (0.1, 0.1, 0.1, 1)] # grey border, white text, light black bg

    def toggle_theme(self, instance):
        app = MDApp.get_running_app()
        if app.theme_cls.theme_style == "Light":
            app.theme_cls.theme_style = "Dark"
            
        else:
            app.theme_cls.theme_style = "Light"
            
        self.update_theme_colors()

    def update_theme_colors(self):
        colors = self.get_button_color()

        # Update toolbar colors
        self.toolbar.md_bg_color = colors[2]
        self.toolbar.specific_text_color = colors[1]

        # Update the colors of all buttons
        for button in self.theme_buttons:
            button.line_color = colors[0]
            button.text_color = colors[1]
            button.md_bg_color = colors[2]

        # Update the theme icon color based on the theme
        if self.theme_icon:
            self.theme_icon.text_color = colors[1]
        app = MDApp.get_running_app()
        if app.theme_cls.theme_style == "Light":
            self.theme_icon.icon = "weather-sunny"
        else:
            self.theme_icon.icon = "weather-night"

    def update_time(self, *args):
        now = datetime.now()
        current_time = now.strftime("%A, %B %d, %Y | %I:%M:%S %p")
        self.toolbar.title = current_time
    
    def build_button(self, text, x=None, y=None, on_press=None):
        button = MDButton(
            md_bg_color=self.get_button_color()[2],
            line_color=self.get_button_color()[0],
            size_hint=(0.3, 0.1)
        )
        button.add_widget(MDButtonText(text=text, text_color=self.get_button_color()[1], font_style="Display", role="small"))
        if x and y:
            button.pos_hint = {"center_x": x, "center_y": y}
        
        if on_press:
            button.bind(on_release=on_press)
        
        self.theme_buttons.append(button)

        return button
    
    def return_home(self, instance, *args):
        app = MDApp.get_running_app()
        app.screen_manager.current = 'home'

    def on_enter(self, *args):
        self.update_theme_colors()
