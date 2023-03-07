# Import math module used in the calculation of compound interest
import math

# First output when the program runs and prompt the user to choose the calculator type
# Used .lower() to accept the user input no matter lower or upper case
print('''
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you have to pay on a home loan 
''')
type = input(str("Enter either 'investment' or 'bond' from the menu above to proceed\n")).lower()

# Conditional statements depending on user input 
# Another conditional statement nested depending on user user input when asking for interest
if type == "investment":
    p = float(input("what is the amount you want to deposit: " ))
    r = float(input("What is the interest rate? "))
    r = r / 100
    t = float(input("How many years do you plan on investing? "))
    interest = str(input("Choose 'simple' or 'compound' interest: ")).lower()
    if interest == "simple":
        simple_calc = round(p * (1 + r * t), 2)
        print(f"Your investment will return {simple_calc}")
    elif interest == "compound":
        compound_calc = round(p * math.pow((1 + r), t), 2)
        print(f"Your investment will return {compound_calc}")

elif type == "bond":
    p = float(input(("What is the present value of the house? ")))
    i = float(input("What is the interest rate? "))
    i = (i / 100) / 12
    n = float(input("How many months do you plan to repay the bond? "))
    bond_calc = round((i * p) / (1 - (1 + i)**(-n)), 2)
    print(f"Your total monthly repayment is {bond_calc}")

# Else statement if user input invalid calculator type at start of program
else:
    print("Please enter an appropriate investment type")