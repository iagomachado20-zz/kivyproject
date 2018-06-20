import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.image import Image

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

class ListApp(App):
    pass

class ListLayout(FloatLayout):
    pass

window = ListApp()
window.run()