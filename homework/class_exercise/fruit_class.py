"""
Create a class Fruit
Define 3 methods in this class
	__init__()
	nutrition()
	fruit_shape()

Print anything you like in these methods

Create one more class (Any fruit name)
This class should inhereit from the Fruit class created above, this
will become the child class and "Fruit" will be referred as parent
class to this class
Define 3 methods in thise class
	__init__()
	nutrition()
	color()
Print anything you like in these methods

Created instances of these classes and call methods from them
Call methods from the base class also using the instance of the
child class
"""

class Fruit(object):
	def __init__(self):
		print("This is a fruit. It has seeds!")

	def nutrition(self):
		print("This fruit is very nutritious.")

	def shape(self):
		print("Fruits can come in all sorts of shapes.")

f = Fruit()
f.nutrition()
f.shape()

	    