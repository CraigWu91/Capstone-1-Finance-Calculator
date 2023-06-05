import math

def investment():
    try:
        p = float(input("What is the amount you want to deposit?: "))
        r = float(input("What is the interest rate? eg 10.25: "))
        r = r / 100
        t = float(input("How many years do you plan on investing?: "))
        while True:
            interest_type = input("Please select either simple or compound interest\n 1)Simple\n 2)Compound\n")
            if interest_type == "1":
                a = round(p * (1 + r*t), 2)
                break
            elif interest_type == "2":
                a = round(p * math.pow((1 + r), t), 2)
                break
            else:
                print("Please select a valid menu option")
        print(f"Your interest returned will be {a}")
    except ValueError:
        print("Please input valid data type")
    

def bond():
    try:
        p = float(input("What is the present value of the house?: "))
        i = float(input("What is the annual interest rate?: "))
        i = (i / 100) / 12
        n = int(input("What is the number of months the bond will be repayed?: "))
        repayment = round((i * p) / (1 - (1 + i)**(-n)), 2)
        print(f"You monthly repayment will be {repayment}")
    except ValueError:
        print("Please input valid data type")

while True:
    calculate = input('''
    Welcome to your financial calculator
    Please select calculator type:
    1)Investment Calculator
    2)Bond Calculator
    0)Exit
    ''')
    if calculate == "1":
        investment()
    elif calculate == "2":
        bond()
    elif calculate == "0":
        exit()
    else:
        print("Please select a valid menu option")
    