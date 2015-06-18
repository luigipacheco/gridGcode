import os
import sys
import fileinput
import this

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.config import Config

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '200')

class UI(BoxLayout):
    def gridgenerator(self):
        x = ObjectProperty()
        y = ObjectProperty()
        px = ObjectProperty()
        py = ObjectProperty()
        countX = 0
        countY = 0
        print (type(self.xv.text))
        print("G90") #Absolute coordenates
        print("G28") # Go home!
        for Y in range(int(int(self.yv.text)/int(self.py.text)+1)):
            countX = 0
            for X in range(int(int(self.xv.text)/int(self.px.text)+1)):
                print("G01 X" + str(countX)+" Y"+str(countY))
                countX = countX + int(self.px.text)
            countY = countY+ int(self.py.text)
        print("G28") # Go home!



class grid(App):
        pass

grid().run()
