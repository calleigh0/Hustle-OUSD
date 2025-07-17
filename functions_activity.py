#Functions Activity - Calleigh Tanaka

Menu = {"Pizza": 2.99, "Burger": 3.99, "Hot dog": 1.99, "Cheese": 0.59, "Ice cream": 1.49, "Churro": 0.79, "Soda": 0.89}

def total_price (item1, item2) :
    total = Menu[item1] + Menu[item2]
    print(f"The total price of {item1} and {item2} is: {total} ")

item1 = input("Enter your first item: ")
item2 = input("Enter you second item: ")
total_price(item1, item2)


def price_difference (item3, item4) :
    difference = (Menu[item3] - Menu[item4])
    print(f"The price difference of {item3} and {item4} is: {difference} ")

item3 = input("Enter your first item: ")
item4 = input("Enter you second item: ")
price_difference(item3, item4)


def inflation (item5, change) :
    inflated_price = Menu[item5] * change
    print(f"The new inflated price  of {item5} is: {inflated_price}")

item5 = input("Enter your item: ")
change = 2
inflation(item5, change)

def deflation (item6, change1) :
    deflated_price = Menu[item6] / change1
    print(f"The new deflated price of {item6} is: {deflated_price}")

item6 = input("Enter your item: ")
change1 = 1.5
deflation(item6, change1)

def add_tax (item7, item8, tax) :
    taxed_total = Menu[item7] + Menu[item8] + tax
    print(f"After tax your total for {item7} and {item8} is: {taxed_total} ")

item7 = input("Enter your first item: ")
item8 = input("Enter you second item: ")
tax = 3.50
add_tax(item7, item8, tax)
