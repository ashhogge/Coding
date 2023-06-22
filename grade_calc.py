grade = int(input("What was your final grade for this class? "))

if grade >= 90:
    letter_grade = "A"
elif grade >= 80 and grade < 90:
    letter_grade = "B"
elif grade >= 70 and grade < 80:
    letter_grade = "C"
elif grade >= 60 and grade < 70:
    letter_grade = "D"
else:
    letter_grade = "F"

remainder = grade % 10

if grade >= 60 and grade < 94:
    if remainder >= 7:
        sign = "+"
    elif remainder < 3 and remainder > 0:
        sign = "-"

if grade >= 70:
    print(f"Congrats, you passed the class with a {letter_grade}{sign}!")
else:
    print(f"You have failed the class with a {letter_grade}{sign}. Reach out to see if you may correct your grade.")
