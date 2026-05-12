# A simple guessing game where the user has to guess a secret number within a certain number of attempts.
secret_number = 9
guess_count = 0
guess_limit = 3
# The user is prompted to enter their guess, and the program checks if the guess is correct. If the user guesses the number correctly, they win. If they run out of attempts, they lose. 
while guess_count < guess_limit:
    guess = int(input("Guess your lucky number: "))
    guess_count +=  1
    if guess == secret_number:
        print("You won!")
        break
# The break statement is used to exit the loop when the user guesses the number correctly.
else:
    print("You failed!")
