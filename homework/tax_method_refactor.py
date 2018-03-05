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
    # federal tax rate is a constant

    fed_sum = gross_income * fed_tax
    state_sum = gross_income * state_tax
    """
	these variables determine how much
	is owed to state and federal institutions
	"""

    net = gross_income - (fed_sum + state_sum)
    # shows how much tax is removed from gross
    return net

# tax rates to be used for different states


co_tax = .0463
# Colorado

il_tax = .0375
# Illinois

ma_tax = .0510
# Massachusetts

pa_tax = .0307
# Pennsylvania

# Salaries of 50K and 100K
salary1 = 50000
salary2 = 100000

net_co1 = net_income(co_tax, salary1)
net_co2 = net_income(co_tax, salary2)

print(net_co1)
print(net_co2)

net_il1 = net_income(il_tax, salary1)
net_il2 = net_income(il_tax, salary2)

print(net_il1)
print(net_il2)

net_ma1 = net_income(ma_tax, salary1)
net_ma2 = net_income(ma_tax, salary2)

print(net_ma1)
print(net_ma2)

net_pa1 = net_income(pa_tax, salary1)
net_pa2 = net_income(pa_tax, salary2)

print(net_pa1)
print(net_pa2)