import random

while True:
    number = random.randint(1, 100)
    guess = int
    guess_count = 0
    print("Guess the magic number!")

    while guess != number:
        guess = int(input("What is your guess? "))
        guess_count +=1

        if guess < number:
            print("Higher")
        elif guess > number: 
            print("Lower")
        else: 
            print("\nYou guessed it!!")
            break

    print("\nTotal guesses:", guess_count)
    print()

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
    else:
        print("Thanks for playing!")