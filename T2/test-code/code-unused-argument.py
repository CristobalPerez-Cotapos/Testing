def example1(x, y, z):
	return x + y

def example2(x, y, z):
	a = y + z
	c = z
	return a + c

class Fruit:

	def __init__(self, name, vitamins):
		self.name = name
		self.vitamins = vitamins

	def change_vitamins(self, vs):
		self.vitamins = []