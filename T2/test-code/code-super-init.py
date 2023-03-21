class Fruit:

	def __init__(self, name, vitamins):
		self.name = name
		self.vitamins = vitamins
		print("Soy una " + self.name)

	def change_vitamins(self, vs):
		self.vitamins = []

class Apple(Fruit):

	def __init__(self):
		super(Apple, self).__init__("manzana", [])

class Pineapple(Fruit):

	def __init__(self):
		print("Soy una piña")
