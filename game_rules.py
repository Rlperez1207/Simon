from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import random
class TestApp(GridLayout):
    def __init__(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Button(text='Hello 1'))
        layout.add_widget(Button(text='World 1'))
        layout.add_widget(Button(text='Hello 2'))
        layout.add_widget(Button(text='World 2'))
class simon(App):
    def build(self):
        return TestApp()

simon().run()

class Game:
  def __init__(self):
    self.state = ["green","red","yellow","blue"]
    self.sequence = [(random.randint(0,3))]
    self.moves = []
    self.game_over=False
  def __repr__(self):
    return "Game({})".format(self.state)

  def __str__(self):
    return "{} {}\n{} {}\n".format(*self.state)

  def move(self):
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
    while not self.game_over:
      print(self)
      print(self.sequence)
      print(self.moves)
      self.move()
      if not self.moves==self.sequence:
        self.game_over = True
        print("YOU LOSE")
      if not self.game_over:
        self.sequence.append(random.randint(0,3))

if __name__ == "__main__":
  a = Game()
  a.play()
