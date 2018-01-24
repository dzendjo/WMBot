# File name: wmbot.py
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('orderform.kv')


class Wmbot(AnchorLayout):
    pass


class WmbotApp(App):
    def build(self):
        return Wmbot()


if __name__== "__main__":
    WmbotApp().run()