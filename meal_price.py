'''
Author: Ashton Hogge

'''

import math

meal_child = float(input("What is the price of a child's meal? "))
meal_adult = float(input("What is the price of an adult's meal? "))

num_child = int(input("\nWhat is the number of children? "))
num_adult = int(input("What is the number of adults? "))
tax_rate = float(input("What is the sales tax rate? "))

subtotal = meal_child * num_child + meal_adult * num_adult
print(f"\nYour subtotal is: ${subtotal: .2f}")

total = float(subtotal + subtotal * tax_rate / 100)
print(f"Your total is: ${total: .2f}")

# I added these lines to round for charity like a normal restaurant/fastfood place would
round_nearest = input("\nWould you like to round your total to the nearest dollar for charity? (yes/no) ")

if round_nearest.lower() == "yes":
    rounded_total = math.ceil(total)
    print(f"\nRounded Total: ${rounded_total}")
    total = rounded_total # updates the total to the rounded total
else:
    print("\nTotal not rounded.")

payment = float(input("\nEnter the payment amount: "))
change = payment - total
if change < 0:
    print("Insufficient amount.")
else: 
    print(f"Payment: ${payment: .2f}")
    print(f"Change: ${change: .2f}")
