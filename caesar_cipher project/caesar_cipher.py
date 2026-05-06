alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    encrypted_text = ""
    for ch in text:
        if not ch.isalpha():
            encrypted_text += ch
            continue
        is_upper = ch.isupper()
        ch = ch.lower()
        new_char= alphabet[(alphabet.index(ch)+shift)%26]
        if is_upper:
            new_char = new_char.upper()
        encrypted_text += new_char
    return encrypted_text

def decrypt(encrypted , shift):
    return encrypt(encrypted , -shift)   

def caesar(original , shift,decision):
    if decision == "encode":
        result = encrypt(original,shift)
        print(f"Your encoded text is {result}")
    elif decision == "decode":
        result = decrypt(original,shift)
        print(f"Your decoded text is {result}")
    
while(True):
    original = input("Enter the text: ")
    shift = int(input("Enter the number of shifts to be done: "))
    decision = input("Enter 'encode' or 'decode' to perform on text: ").lower()
    caesar(original,shift,decision)
    can_continue = input("Do you wish to continue? y/n: ").lower()
    if can_continue=="n":
        print("Thank you!")
        break





