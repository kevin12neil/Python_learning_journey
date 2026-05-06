import random

print(
    "Welcome to the coin flip simulator!\n"
    "Specify the target ratio for heads to tails, simulate flipping a coin multiple times,\n"
    "and track how many retrials it takes to achieve that ratio."
)
print("__________________________________________________________________________________________________________________")
n = int(input("\nEnter the number of coin flips you want each trial to have:\n"))
print("__________________________________________________________________________________________________________________")
counter = 0
heads = []
tails = []
while n%2 != 0 or n <= 0:
    print("\nInvalid input. Please enter a positive even integer.")
    print("__________________________________________________________________________________________________________________")
    n = int(input("\nEnter the number of coin flips you want each trial to have:\n"))
target_ratio = float(input("\nEnter your desired ration for heads to tails in float value (e.g. 0.5 for 50% heads):\n"))
while target_ratio < 0 or target_ratio > 1:
    print("\nInvalid input. Please enter a float value between 0 and 1. \nA value around 0.5 usually gives the fastest results since the probability of heads and tails is equal.")
    print("__________________________________________________________________________________________________________________")
    target_ratio = float(input("\nEnter your desired ration for heads to tails in float value (e.g. 0.5 for 50% heads):\n"))

def randomhot(n,target_ratio):
    global counter
    
    while True:
        counter += 1
        heads = []
        tails = []

        for  i in range(n):
            HoT = random.randint(1, 2)
            if HoT != 1:
                tails.append("Tails")
            else:
                heads.append("Heads")
        if len(heads)==target_ratio*n:
            break
    return heads,tails

print("__________________________________________________________________________________________________________________")
print(f"\nOur target ratio is {int(target_ratio*n)} heads to {int(n - target_ratio*n)} tails.")
print("")
print("Flipping the coin...")
heads,tails=randomhot(n,target_ratio)


print("__________________________________________________________________________________________________________________")
print("\nHeads appeared:",len(heads))
print("Tails appeared:", len(tails))
print("Experiment has been repeated:",str(counter) +" times")

next_step = input("\nDo you want to try again? (y/n):\n")
while next_step.lower() == 'y':
    counter = 0
    heads = []
    tails = []
    n = int(input("\nEnter the number of coin flips you want each trial to have:\n"))
    print("__________________________________________________________________________________________________________________")
    while n%2 != 0 or n <= 0:
        print("\nInvalid input. Please enter a positive even integer.")
        print("__________________________________________________________________________________________________________________")
        n = int(input("\nEnter the number of coin flips you want each trial to have:\n"))
    target_ratio = float(input("\nEnter your desired ration for heads to tails in float value (e.g. 0.5 for 50% heads):\n"))
    while target_ratio < 0 or target_ratio > 1:
        print("\nInvalid input. Please enter a float value between 0 and 1. \nA value around 0.5 usually gives the fastest results since the probability of heads and tails is equal.")
        print("__________________________________________________________________________________________________________________")
        target_ratio = float(input("\nEnter your desired ration for heads to tails in float value (e.g. 0.5 for 50% heads):\n"))
    
    print("__________________________________________________________________________________________________________________")
    print(f"\nOur target ratio is {int(target_ratio*n)} heads to {int(n - target_ratio*n)} tails.")
    print("")
    print("Flipping the coin...")
    heads,tails=randomhot(n,target_ratio)
    
    
    print("__________________________________________________________________________________________________________________")
    print("\nHeads appeared:",len(heads))
    print("Tails appeared:", len(tails))
    print("Experiment has been repeated:",str(counter) +" times")
    
    next_step = input("\nDo you want to try again? (y/n):\n")
    
else:
    print("\nThank you for using the coin flip simulator!")

