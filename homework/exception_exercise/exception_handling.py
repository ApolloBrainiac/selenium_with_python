"""
Exception Handling Exercise

Create a dictionary "car"
Create 3 keys
	- make
	- model
	- year

Try to access the color key. Remember, we never created the color key,
so it's going to throw an exception. You need to handle the exception
using try, except and finally block
"""
# Color access function
def pick_color():
	try:
		print('Oh my ex-girlfriend\'s car is ' + car['color'] + '.')
	except:
		print('You know, I don\'t really remember what color her car is.')
	finally:
		print('Actually, all my ex\'s drive Jettas. Weird now that I think about it.')


# Car dictionary
car = {'make': 'VW', 'model': 'Jetta', 'year': '2005'}