from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
import random

class Widgets(Widget):
    pass
class TestApp(GridLayout):
    def __init__(self,**kwargs):
        super(TestApp,self).__init__(**kwargs)#use multi inheritence
        self.cols = 2
        self.add_widget(Button(text='Green'))
        self.add_widget(Button(text='Red'))
        self.add_widget(Button(text='Yellow'))
        self.add_widget(Button(text='Blue'))

class The_game(Widget):
  score = NumericProperty(0)
  pick = ObjectProperty(None)
  sequence = ObjectProperty(None)
  z = ObjectProperty(None)
  r = ObjectProperty(None)
  yellow = ObjectProperty(None)
  green = ObjectProperty(None)
  def init(self):
      self.state = [self.green,self.red,self.yellow,self.blue]
      self.moves = []
      self.game_over = False
      self.r = int(1)
      self.z = int(0)
      self.sequence = [(random.choice(self.state))]

  def check(self):
      self.score += len([self.sequence])
      for i in range(len([self.sequence])):
        self.pick = 6
  def win(self):
      if not self.moves==self.sequence:
        self.game_over = True
        Label(text="You Lose")
      if not self.game_over:
        self.sequence.append(random.choice(self.state))

  def move(self):
    while True:
        self.moves = []
        if self.pick in range(0,3):
            self.check()
            self.moves.append(int(self.pick))
            self.pick = 6
        if self.pick == 6:
            for i in range(len(self.sequence)):
                self.sequence[0] = 0,0,0,1
  def play(self):
    self.game_over = False
    while not self.game_over:
      self.move()
      self.win()
class simon(App):
    def build(self):
        re= The_game()
        return re

if __name__ == "__main__":
  simon().run()
