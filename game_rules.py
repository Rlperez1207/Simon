import random
class Game:
  def __init__(self):
    self.state = ["green","red","yellow","blue"]
    self.sequence = []
  def __repr__(self):
    return "Game({})".format(self.state)
    
  def __str__(self):
    return "{} {}\n{} {}\n".format(*self.state)
    
  def has_lost(self,moves):
    if moves == self.sequence:
      return False
    print("LOST")
  def move(self):
    while True:
      try:
        pick = str(input("Pick a color dude: "))
        moves = int(pick)
        self.sequence.append(random.randint(0,3))
        if moves not in range(4):
          raise ValueError
        break
      except ValueError:
        print("I dont know what you did but its wrong")
  def play(self):
    while not self.has_lost:
      print(self)
      self.move()
      print(self.sequence)
      if self.has_won(you):
        print('{} wins'.format(you))
        self.game_over = True
        print(self)
        break
    
a = Game()
a.play()
    
    
