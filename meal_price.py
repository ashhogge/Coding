'''
Author: Ashton Hogge

'''

import math

meal_child = float(input("What is the price of a child's meal? "))
meal_adult = float(input("What is the price of an adult's meal? "))

print()

num_child = int(input("What is the number of children? "))
num_adult = int(input("What is the number of adults? "))
tax_rate = float(input("What is the sales tax rate? "))

print()

subtotal = meal_child * num_child + meal_adult * num_adult
print(f"Your subtotal is: ${subtotal: .2f}")

total = float(subtotal + subtotal * tax_rate / 100)
print(f"Your total is: ${total: .2f}")

print()

round_nearest = input("Would you like to round your total to the nearest dollar? (yes/no) ")
if round_nearest.lower() == "yes":
    rounded_total = round(total)
    print(f"Rounded Total: ${rounded_total}")
    total = rounded_total # updates the total to the rounded total
else:
    print("Total not rounded.")

print()

payment = float(input("Enter the payment amount: "))
change = payment - total
print(f"Payment: ${payment: .2f}")
print(f"Change: ${change: .2f}")
