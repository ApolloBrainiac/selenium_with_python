"""
Execute statements repeatedely
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""

my_string = 'abcabc'

for c in my_string:
	if c == 'a':
		print('A', end=' ')
	else:
		print(c, end=' ')

cars = ['bmw', 'benz', 'honda']

for car in cars:
	print(car)

nums = [1, 2, 3]

for n in nums:
	print(n * 10, end= ' ')

d = {'one': 1, 'two': 2, 'three': 3}
for k in d:
	print(k + " " + str(d[k]), end=" ")

print("*"*20)

for k,v in d.items():
	print(k)
	print(v)