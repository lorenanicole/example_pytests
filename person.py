import random

class Person(object):
	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def age(self):
		return len(self.name) * 3

	def randomize_age(self):
		return random.randrange(15,49) * 2
