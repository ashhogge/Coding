'''
Author: Ashton Hogge

Purpose: Practicing
'''

print("Please enter the following information:")

# Blank lines
print()

first = input("First name: ")
last = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
# additional info
height = input("Height: ")
weight = input("Weight: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")

# This time I used a \n to make a blank line before this:
print("\nThe ID Card is:")
print("----------------------------------------")
print(f"{last.upper()}, {first.capitalize()}")
print(job_title.title())
print(f"ID: {id_number}")
print("Height:", height)
print("Weight:", weight)
print()
print(email.lower())
print(phone)
print("----------------------------------------")


