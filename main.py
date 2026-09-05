from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# Set background color (Dark theme)
Window.clearcolor = (0.08, 0.08, 0.1, 1)

class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Title Label
        title = Label(
            text="[b]DEAD RIVERS[/b]",
            markup=True,
            font_size='36sp',
            color=(0.9, 0.2, 0.2, 1),
            size_hint=(1, 0.4)
        )
        
        # Buttons
        start_btn = Button(
            text="Start Game",
            font_size='20sp',
            background_color=(0.2, 0.6, 0.2, 1),
            size_hint=(1, 0.2)
        )
        start_btn.bind(on_press=self.go_to_game)
        
        exit_btn = Button(
            text="Exit",
            font_size='20sp',
            background_color=(0.6, 0.2, 0.2, 1),
            size_hint=(1, 0.2)
        )
        exit_btn.bind(on_press=App.get_running_app().stop)
        
        layout.add_widget(title)
        layout.add_widget(start_btn)
        layout.add_widget(exit_btn)
        
        self.add_widget(layout)
        
    def go_to_game(self, instance):
        self.manager.current = 'game'

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.status_label = Label(
            text="Exploration Mode\nTap action to proceed.",
            font_size='18sp',
            halign='center',
            size_hint=(1, 0.6)
        )
        
        action_btn = Button(
            text="Action",
            font_size='18sp',
            background_color=(0.2, 0.4, 0.8, 1),
            size_hint=(1, 0.2)
        )
        action_btn.bind(on_press=self.perform_action)
        
        back_btn = Button(
            text="Back to Menu",
            font_size='16sp',
            size_hint=(1, 0.2)
        )
        back_btn.bind(on_press=self.go_to_menu)
        
        layout.add_widget(self.status_label)
        layout.add_widget(action_btn)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
        
    def perform_action(self, instance):
        self.status_label.text = "You ventured deeper down the river..."
        
    def go_to_menu(self, instance):
        self.manager.current = 'menu'

class DeadRiversApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        return sm

if __name__ == '__main__':
    DeadRiversApp().run()
