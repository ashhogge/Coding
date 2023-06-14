'''
Author: Ashton Hogge

Comment: This program uses variables and displays them in an ad-lib story

'''

print("Let's create an ad-lib story!")
print("Please provide the following inputs:")

name = input("Enter a name: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
verb = input("Enter a verb: ")

print("\nOnce upon a time, in a", adjective1, "land, there lived a brave adventurer named", name.capitalize() + ".")
print(name.capitalize(), "had a", adjective2, noun1.capitalize() + " that was rumored to have magical powers.")
print("One day, while exploring the", noun2.capitalize() + ",", name.capitalize(), "encountered a wise old man.")
print("The man told", name.capitalize(), "that the fate of the kingdom depended on their ability to", verb + ".")
print(name.capitalize(), "accepted the challenge and embarked on an long journey.")
print("During their quest,", name.capitalize(), "encountered dangerous creatures, solved challenging riddles, and overcame countless obstacles.")
print("With each triumph, their", noun1.capitalize(), "grew stronger, and their determination to save the kingdom deepened.")
print("Finally, after a long journey,", name.capitalize(), "reached the heart of the", noun2.capitalize() + ".")
print("With a mighty", verb + ",", name.capitalize(), "unleashed the power of their", adjective2, noun1.capitalize() + " and restored peace to the land.")
print("The kingdom rejoiced, and", name.capitalize(), "became a legend, forever remembered for their bravery and heroism.")
