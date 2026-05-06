auction_bids = {}

while True:
    name = input("Enter your name: ")
    bid = float(input("Enter your bid amount: $"))
    auction_bids[name] = bid
    print("Your bid has been recorded.")
    can_continue = input("Are there any other bidders? type 'yes' or 'no' : ").lower()
    if(can_continue == "no"):
        break
    else:
        print("\n"*100) #acts as a way to clear the screen

final = ""
highest_bid = 0

for name,bid in auction_bids.items():
    if bid > highest_bid:
        final = name
        highest_bid = bid
    
print(f"The highest bidder is {final} with a bid of ${highest_bid:.2f}")
