def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b

def calculator(x):
    operator = input("+\n-\n*\n/\nEnter the operation to perform: ")
    y = float(input("What is the next number? :"))
    if operator=="+":
        result = add(x,y)
    elif operator=="-":
        result = subtract(x,y)
    elif operator=="*":
        result = multiply(x,y)
    elif operator=="/":
        if y==0:
            print("Error: division by zero")
            return x
        result = divide(x,y)
    else:
        print("Invalid operator.")
        return x
    print("---------------------------------------------")
    print(f"{x} {operator} {y} = {result}")
    print("---------------------------------------------")
    return result


while True:
    exit_all = False
    x = float(input("what is the first number: "))
    x = calculator(x)
    while True:
        decision = input(
            f"Type 'y' to continue calculating with {x}\n"
            "Type 'n' to start a new calculation\n"
            "Type 'e' to exit\n" 
            "decision : "
            ).lower()
        if decision == 'e':
            print("Thank you!")
            exit_all = True
            break
        elif decision == 'n':
            break
        elif decision == 'y':
            x = calculator(x)
    if exit_all == True:
        break