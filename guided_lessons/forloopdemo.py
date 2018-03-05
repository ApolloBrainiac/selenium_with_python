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