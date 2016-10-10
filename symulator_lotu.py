import random
import time

class symulator():
	def __init__(self,angle):
		self.angle=angle
	def add_correction(self,correction):
		self.angle=self.angle+correction
	def run(self):
		while 1:
			r=random.gauss(0,50)
			correction=r
			if self.angle > 90:
				correction=-r
			print "angle: %d"%self.angle			
			self.add_correction(correction)	
			print "correction: %d"%correction
			print "------------"	
			time.sleep(1)	
			
			



samolot=symulator(10)
samolot.run()

