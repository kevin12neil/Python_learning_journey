import random
from art import logo
def check(guess,lives,game_over):
    """checks if the geuss is right and returns appropriate life count."""
    if guess==original_number:
        print("=======================================================")
        print(f"You have guessed the Correct number {original_number} in {original_life_count - lives+1} tries! You win!")
        print("=======================================================")
        game_over = True
    elif guess<original_number:
        lives = lives-1
        if lives>0:
            print("=======================================================")
            print(f"Too Low.\nGuess again.\nYou have {lives} attempts remaining.")
    elif guess>original_number:
        lives = lives-1
        if lives>0:
            print("=======================================================")
            print(f"Too High.\nGuess again.\nYou have {lives} attempts remaining.")
    if lives==0:
        print("=======================================================")
        print(f"You Lose! The number I thought of was {original_number}.")
        print("=======================================================")
    return lives,game_over

print(logo)
print("Welcome to the Number Guessing Game!\n")

while True:
    decision = input("Im thinking of a number between 1 and 100.\nChoose a difficulty , type 'easy' or 'hard': ").lower()

    game_over = False

    if decision=='easy':
        lives = 10
    elif decision=='hard':
        lives = 5
    else:
        print("Choose a valid difficulty.")
        continue

    original_life_count = lives
    original_number = random.randint(1,100)

    while lives > 0:
        guess = int(input("Make a guess: "))
        lives,game_over = check(guess,lives,game_over)
        if game_over:
            break

    can_continue = input("Do you wish to continue? y/n: ").lower()
    if can_continue=='n':
        print("Thank you for playing!")
        break

    