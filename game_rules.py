from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
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

  def move(self):
    self.state = ["green","red","yellow","blue"]
    self.sequence = [(random.randint(0,3))]
    self.moves = []
    self.game_over = False
    while True:
      try:
        self.moves = []
        for i in range(len(self.sequence)):
          pick = str(input("Pick a color dude: "))
          self.moves.append(int(pick))
        if self.moves[-1] not in range(4):
          raise ValueError
        break
      except ValueError:
        print("I dont know what you did but its wrong")
        print(self)
  def play(self):
    self.game_over = False
    while not self.game_over:
      self.move()
      if not self.moves==self.sequence:
        self.game_over = True
        print("YOU LOSE")
      if not self.game_over:
        self.sequence.append(random.randint(0,3))
class simon(App):
    def build(self):
        re= The_game()
        re.play()
        return re

if __name__ == "__main__":
  simon().run()
