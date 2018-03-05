"""
Create a method, which takes the state and gross income
as arguments and returns the net income after deducting
tax based on the state.

Assume Federal Tax: 10%
Assume state tax on your wish.

You don't have to do for all the states, just take 3-4 to solve
the purpose of the exercise
"""
def net_income(state_tax, gross_income):
	fed_tax = .1
	fed_sum = gross_income * fed_tax
	state_sum = gross_income * state_tax
	net = gross_income - (fed_sum + state_sum)
	return net

