class Student:
    def __init__(self, name):
      self.name = name
      self.gladness = 10
      self.progress = 0
    def study(self):
      self.gladness += 20
      self.progress -= 10
      print('Study time')
    def chill(self):
      self.gladness += 35
      self.progress -= 8
      print('Chill time')
    def sleep(self)
      self.gladness += 4
      print('Sleep time')