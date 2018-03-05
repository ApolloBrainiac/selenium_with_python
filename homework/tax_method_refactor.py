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
    total_tax = fed_sum + state_sum
    """
    these variables determine how much
    is owed to state and federal institutions
    """

    net = gross_income - total_tax
    # shows how much tax is removed from gross
    print(net)


"""
State Tax rates for:
Colorado
Illinois
Massachusetts
Pennsylvania
placed into a dictionary
"""

state_rates = {"co_tax": .0463, "il_tax": .0375,
               "ma_tax": .0510, "pa_tax": .0307}

# Salaries of 50K and 100K
salary1 = 50000
salary2 = 100000

# Loops through and prints each salary/tax rate combination
for x in state_rates:
    net_income(state_rates[x], salary1)
    net_income(state_rates[x], salary2)
    print("*" * 20)
