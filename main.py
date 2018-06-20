import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.button import Button

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')


class MainApp(App):
    pass


class MainLayout(FloatLayout):

    def lista(self, pag):
        

window = MainApp()
window.run()