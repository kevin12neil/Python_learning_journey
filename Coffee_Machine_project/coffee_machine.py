from data_set import MENU, resources
from art import preparing, coffee_cup

def clear_inserted_coins(inserted_coins):
    """clears the inserted_coins dictionary"""

    inserted_coins["pennies_count"] = 0
    inserted_coins["nickles_count"] = 0
    inserted_coins["dimes_count"] = 0
    inserted_coins["quarters_count"] = 0

def make_recipe(resources, order, menu):
    """deducts the quantity of resources used in our recipe from machine resources"""

    resources["water"] -= menu[order]["ingredients"]["water"]
    resources["coffee"] -= menu[order]["ingredients"]["coffee"]
    if not order == "espresso":
        resources["milk"] -= menu[order]["ingredients"]["milk"]
    print(preparing)
    print("=======================================================")
    print(f"Here is your {order}☕. Enjoy!")
    print("=======================================================")

def refill_resources(resources):
    """refills the machine to original state"""

    # "water": 300,
    # "milk": 200,
    # "coffee": 100,
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100


def calculate_money(inserted_coins):   
    """helper function to calculate the total money from coins stored in machine"""

    return inserted_coins["pennies_count"]*0.01 + inserted_coins["nickles_count"]*0.05 + inserted_coins["dimes_count"]*0.10 + inserted_coins["quarters_count"]*0.25


def check_money(inserted_coins, final_money, menu, order, sufficient_money):
    """Checks the recipe cost and informs if coins given are sufficient to continue"""

    #check if the coins are sufficient
    if calculate_money(inserted_coins) == menu[order]["cost"]:
        print("Perfect! Your order is being prepared.")
        final_money += menu[order]["cost"]
    elif calculate_money(inserted_coins) > menu[order]["cost"]:
        print(f"Your order is being prepared.\nHere is ${(calculate_money(inserted_coins) - menu[order]['cost']):.2f} in change.")
        final_money += menu[order]["cost"]
    else:
        print(f"Sorry that is not enough money. Money refunded.")
        sufficient_money = False
    return sufficient_money, final_money


def take_money(inserted_coins):
    """Takes the numebr of coins provided by user"""
    print("\n*******************************************************")
    inserted_coins["pennies_count"] = int(input("Enter number of pennies: "))
    inserted_coins["nickles_count"] = int(input("Enter number of nickles: "))
    inserted_coins["dimes_count"] = int(input("Enter number of dimes: "))
    inserted_coins["quarters_count"] = int(input("Enter number of quarters: "))
    print("\n*******************************************************")


def check_resources(order, menu, resources, sufficient_materials):
    """assigns boolean value False if not enough water, milk, or coffee are present in resources and prints a statement about it"""

    if resources["water"] < menu[order]["ingredients"]["water"]:
        sufficient_materials["water"] = False
        print("Sorry there is not enough water.")
    
    if not order == "espresso":
        if resources["milk"] < menu[order]["ingredients"]["milk"]:
            sufficient_materials["milk"] = False
            print("Sorry there is not enough milk.")

    if resources["coffee"] < menu[order]["ingredients"]["coffee"]:
        sufficient_materials["coffee"] = False
        print("Sorry there is not enough coffee.")

    
def process_order(order, MENU, resources, inserted_coins, final_money, sufficient_materials, machine_off):
    """Processing the order given by user"""

    if order == "off":
        machine_off = True

    elif order == "refill":
        refill_resources(resources)

    elif order == "report":
        print("=======================================================")
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {final_money:.2f}")
        print("=======================================================")

    elif order == "espresso" or order == "latte" or order == "cappuccino":

        sufficient_materials["water"] = True 
        sufficient_materials["milk"] = True
        sufficient_materials["coffee"] = True

        check_resources(
            order, 
            MENU, 
            resources, 
            sufficient_materials
        )
        
        if sufficient_materials["water"] and sufficient_materials["coffee"] and sufficient_materials["milk"]:
            take_money(inserted_coins)
            sufficient_money = True
            sufficient_money, final_money = check_money(inserted_coins, final_money, MENU, order, sufficient_money)
            if sufficient_money:
                make_recipe(resources, order, MENU)
            clear_inserted_coins(inserted_coins)

        else:
            print("Not enough resources to proceed. Please refill the resources in machine.")

    else:
        print("Invalid order. Please try again.")
    
    return machine_off,final_money


#initializing variables for amchine moeny , materail sufficiency , final money etc...
inserted_coins = {}
sufficient_materials = {}
machine_off = False
inserted_coins["pennies_count"] = 0
inserted_coins["nickles_count"] = 0
inserted_coins["dimes_count"] = 0
inserted_coins["quarters_count"] = 0
final_money = 0.0

print(coffee_cup)
print("\n*******************************************************")
print("Special commands!\nrefill - Refills the machine resources\nreport - Generates a report on the machine resources\noff - Turns off the machine\nNote: type these commands in the input window.")
print("\n*******************************************************")

while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    machine_off, final_money = process_order(
        order, 
        MENU,
        resources, 
        inserted_coins,
        final_money,
        sufficient_materials,
        machine_off
    )
    if machine_off:
        print("Thank you for using the machine!\nPowering off....")
        break