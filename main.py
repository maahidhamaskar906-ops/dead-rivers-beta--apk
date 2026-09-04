import socket
import threading
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class DeadRiversGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.van_x = 300
        self.van_y = 100
        self.fuel = 100.0
        self.zombie_y = 800
        self.zombie_x = 300

        # Render elements
        with self.canvas:
            # Road
            Color(0.2, 0.2, 0.2, 1)
            Rectangle(pos=(200, 0), size=(400, 2000))
            
            # Van
            Color(0.8, 0.1, 0.1, 1)
            self.van_graphic = Rectangle(pos=(self.van_x, self.van_y), size=(60, 100))
            
            # Zombie
            Color(0.1, 0.8, 0.2, 1)
            self.zombie_graphic = Ellipse(pos=(self.zombie_x, self.zombie_y), size=(40, 40))

        # Game Loop
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):
        # Update fuel and move environment
        if self.fuel > 0:
            self.fuel -= 0.05
            self.zombie_y -= 3
            if self.zombie_y < -50:
                self.zombie_y = 1000

        # Update visuals
        self.van_graphic.pos = (self.van_x, self.van_y)
        self.zombie_graphic.pos = (self.zombie_x, self.zombie_y)

    def move_left(self):
        if self.van_x > 210:
            self.van_x -= 15

    def move_right(self):
        if self.van_x < 530:
            self.van_x += 15

    def refuel(self):
        self.fuel = min(100.0, self.fuel + 20.0)

class DeadRiversApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        self.game = DeadRiversGame()
        
        # Overlay UI
        ui = BoxLayout(size_hint_y=0.2)
        btn_left = Button(text="< Left")
        btn_right = Button(text="Right >")
        btn_fuel = Button(text="+ Add Coal")

        btn_left.bind(on_press=lambda x: self.game.move_left())
        btn_right.bind(on_press=lambda x: self.game.move_right())
        btn_fuel.bind(on_press=lambda x: self.game.refuel())

        ui.add_widget(btn_left)
        ui.add_widget(btn_fuel)
        ui.add_widget(btn_right)

        root.add_widget(self.game)
        root.add_widget(ui)
        return root

if __name__ == '__main__':
    DeadRiversApp().run()
      
