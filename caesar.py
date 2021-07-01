
def menu():
    print("Welcome to Caeser Cipher!")
    val = input("Enter 1 to encrypt or 2 to decrypt: ")
    if val == "1":
        msg = input("Message: ")
        shift = input("Shift: ")
        encrypt(msg,shift)
    
    elif val == "2":
        encrypted = input("Encrypted: ")
        shift = input("Shift (leave blank if you don't know): ")
        
        if shift == "":
            decrypt(encrypted)
            
        else:
            decrypt(encrypted, shift)

    else:
        print("That is not an option")

def encrypt(msg, shift):
    return "placeholder1"

def decrypt(encrypted, shift):
    return "placeholder2"


def decrypt(encrypted):
    # Bruteforce
    return "placeholder3"



menu()


