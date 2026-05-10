import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def ace_check(hand):
    """makes the ace value 1 if we require it"""
    x = hand.copy()
    ind = 0
    if(sum(hand)>21):
        for i in range(len(x)):
            if x[i] == 11:
                x[i] = 1
                ind = i
                break
        if sum(x) <= 21: #ace can be made to have value 1
            hand[ind] = 1
    
def set_dealer(hand):
    """This function sets the dealer to have over or equal to 17 value in his hand"""
    while(sum(hand)<17):
        hand.append(random.choice(cards))

def display_victor(player_hand,dealer_hand):
    """displays the victor of the game"""
    print(f"Player hand: {player_hand}\nPlayer value: {sum(player_hand)}\nDealer hand: {dealer_hand}\nDealer value: {sum(dealer_hand)}")
    print("=======================================================")
    #Case 1 : immediate loss ; player has more than 21 value.
    if(sum(player_hand)>21):
        print("BUSTED! You lose!")
    #Case 2 : win ; player hand < dealer hand BUT dealer is over 21
    elif(sum(dealer_hand)>21):
        print("You WIN! Dealer is BUSTED!")
    #Case 3 : loss ; player hand < dealer hand => dealer wins.
    elif(sum(player_hand)<sum(dealer_hand)):
        print("You LOSE! Dealer wins!")
    #Case 4 : draw ; player hand = dealer hand => its a draw
    elif(sum(player_hand)==sum(dealer_hand)):
        print("It's a DRAW! Nobody wins!")
    #Case 5 : victory ; player hand > dealer hand => you win!
    else:
        print("You WIN! Congratulations!!")
    print("=======================================================")  

def check_validity(hand):
    """returns true if cards add up to or more than 21"""
    ace_check(hand)
    if (sum(hand)>21):
        return True
    return False

def blackjack():
    player_blackjack = False
    dealer_blackjack = False
    player_hand = []
    dealer_hand = []
    game_over = False
    for i in range(2):
        player_hand.append(random.choice(cards))
        dealer_hand.append(random.choice(cards))
    print("*******************************************************")
    print(f"Your cards are: {player_hand}\nPlayer value: {sum(player_hand)}\nDealer's revealed card is: {dealer_hand[0]}")
    print("*******************************************************")
    if(sum(player_hand)==21):
        player_blackjack = True
    elif(sum(dealer_hand)== 21):
        dealer_blackjack = True

    if player_blackjack and dealer_blackjack:
        print(f"Player hand: {player_hand}\nPlayer value: {sum(player_hand)}\nDealer hand: {dealer_hand}\nDealer value: {sum(dealer_hand)}")
        print("=======================================================")
        print("It's a DRAW!")
        print("=======================================================")
    elif player_blackjack:
        print(f"Player hand: {player_hand}\nPlayer value: {sum(player_hand)}\nDealer hand: {dealer_hand}\nDealer value: {sum(dealer_hand)}")
        print("=======================================================")
        print("Congrats! you have hit Blackjack!")
        print("=======================================================")
    else:
        while True:
            player_decision = input("\nDo you wish to hit or stand : \n").lower()
            if (player_decision == 'hit'):
                if(sum(player_hand)==21):
                    print("\n*******************************************************")
                    print(f"Your current hand is: {player_hand}\nPlayer value: {sum(player_hand)}\nDealer's revealed card is: {dealer_hand[0]}")
                    print("*******************************************************\n")
                    print("It is advised to Stand now. You have hit 21 in value.")
                else:
                    player_hand.append(random.choice(cards))
                    game_over = check_validity(player_hand)
                    print("\n*******************************************************")
                    print(f"Your current hand is: {player_hand}\nPlayer value: {sum(player_hand)}\nDealer's revealed card is: {dealer_hand[0]}")
                    print("*******************************************************\n")
            elif(player_decision == 'stand'):
                set_dealer(dealer_hand) #making sure dealer has over or equal to 17 in his hand.
                game_over = True
            else:
                print("Please enter either 'hit' or 'stand'.")
            if game_over:
                break
        ace_check(dealer_hand)
        ace_check(player_hand)
        display_victor(player_hand,dealer_hand)
    
print("""88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"      """)

while True:
    
    decision = input("\nDo you want to play blackjack? y/n: ").lower()
    print("\n")
    if decision == 'y':
        blackjack()
    else:
        print("Thank you!")
        break