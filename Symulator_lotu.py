import random
import time
from Samolot import Samolot

class Symulator(object):

  def __init__(self):
    self.samolot=Samolot(float(random.gauss(90,100)))
    
  def run(self):
    while True:
      print "angle: %f"%self.samolot.angle
      self.samolot.turbulence()
      print "angle after turbulence: %f"%self.samolot.angle	
      correction=self.samolot.generate_correction()
      print "correction: %f"%correction		
      self.samolot.add_correction(correction)		
      print "new angle: %f"%self.samolot.angle	
      print "------------"	
      time.sleep(1)	  

			
if __name__=="__main__":
  samolot=Symulator()
  samolot.run()

