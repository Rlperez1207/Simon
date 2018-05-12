import random
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
      self.move()
      self.sequence.append(random.randint(0,3))
      if self.moves[-1]==self.sequence[-1]:
        self.game_over = True
        print(self)
        print(self.sequence)
        break
    
if __name__ == "__main__":
  a = Game()
  a.play()
    
    
