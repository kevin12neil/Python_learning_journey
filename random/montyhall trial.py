import random
doors = [1, 2, 3]
counter = 0
n = int(input("\nEnter the number of trials you want to run:\n"))

lossy = 0
winy = 0
lossn = 0
winn = 0
while counter < n:
    counter += 1
    win_door = random.choice(doors)
    player_choice = random.choice(doors)
    if win_door==player_choice:
        lossy +=1
    else:
        winy+=1
    
    if win_door==player_choice:
         winn+=1
    else:
        lossn+=1
print("ratio of winning when switching:",winy/n)
print("ratio of winning when not switching:",winn/n)
print("number of wins when switching:",winy)
print("number of wins when not switching:",winn)
print("\nThank you for using the Monty Hall simulator. Goodbye!")   