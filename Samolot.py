import random

class Samolot(object):

  def __init__(self,angle):
    self.angle=float(angle)
    
  def add_correction(self,correction): 
      self.angle+=float(correction)
      
  def generate_correction(self):
    return -self.angle/2.0
    
  def turbulence(self):
    turbulence=float(random.gauss(5,10))
    print "turbulence: %f"%turbulence
    self.angle+=turbulence

