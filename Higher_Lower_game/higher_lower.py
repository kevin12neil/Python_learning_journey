import random
from art import logo,vs
from game_data import data

def get_choice_B(ch_A,data):
    """generating a choice_B that doesn't match choice_A"""
    ch_B = random.randint(0, len(data) - 1)
    while ch_B==ch_A:
        ch_B = random.randint(0, len(data) - 1)
    return ch_B

def check_decision(decision, a_followers, b_followers, game_over, score):
    """checks the decision and returns either a score increment or causes game over to be True"""
    if decision == 'a':
        if a_followers > b_followers:
            score+=1
        else:
            game_over = True
    elif decision == 'b':
        if b_followers > a_followers:
            score+=1
        else:
            game_over = True
    else:
        print("Invalid input.")
    return score, game_over

def start_game():
    """this function begins the game and can be called later for replay functionality"""
    #initialize our score and game_over
    score = 0
    game_over = False

    #pick the first choice A
    choice_A = random.randint(0, len(data) - 1)

    while not game_over:
        choice_B = get_choice_B(choice_A, data)
        if score>0:
            print(f"You're right! Current score: {score}")

        #print out our two choices to be compared
        print("=======================================================")
        print(
            f"Compare A: {data[choice_A]['name']}, "
            f"a {data[choice_A]['description']}, "
            f"from {data[choice_A]['country']}"
        )
        print(vs)
        print(
            f"Compare B: {data[choice_B]['name']}, "
            f"a {data[choice_B]['description']}, "
            f"from {data[choice_B]['country']}"
        )
        print("=======================================================")

        #check our decision
        decision = input("Who has more followers? Type 'A' or 'B': ").lower()
        score, game_over = check_decision(decision, data[choice_A]['follower_count'], data[choice_B]['follower_count'], game_over, score)

        #updating choice_A
        choice_A = choice_B

    #user has lost if while loop terminates
    print(f"Sorry, that's wrong. Final score: {score}")

#Logo and asking user to begin
print(logo)
can_continue = True
while can_continue:
    start = input("Do you want to play Higher, Lower? y/n: ").lower()
    if start == 'y':
        start_game()
    elif start == 'n':
        print("Thank you!")
        can_continue = False
    else:
        print("Please enter valid decision.")
