# Author: Ashton Hogge
# I added a little bet where you try to guess how many attempts it will take the user. 

secret = "weekend"

print("Welcome to the word guessing game! There are 7 letters in the secret word.")
bet = int(input("\nHow many attempts do you think it will take you?")) # this is the extra part, where you try to guess the amount of tries it will take you!

if bet <= 0: 
    print("Please enter a positive number for your bet.")
    exit()

print("\nBet saved as", bet)

guess = input("\nWhat is your guess? ").lower()

guess_count = 1

while guess != secret:
    if len(guess) != 7:
        print("Your guess must have the same number of letters as the secret word.")
    else:
        hint = ""
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                hint += guess[i].upper()
            elif guess[i] in secret:
                hint += guess[i].lower()
            else:
                hint += "_"
        
        print("Your hint is:", hint)
    
    guess = input("What is your guess? ").lower()
    guess_count += 1
    

print("Congratulations! You guessed the word correctly!")
print("Total guesses:", guess_count)

if bet == guess_count: #this is where you will see if you got your bet right
    print("Wow! You guessed your bet correctly!")
else:
    print("You did not guess your bet correctly.")
