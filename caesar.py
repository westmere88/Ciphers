
def menu():
    print("Welcome to Caeser Cipher!")
    val = input("Enter 1 to encrypt or 2 to decrypt: ")
    
    if val == "1":
        msg = input("Message: ")
        
        
        shift = input("Shift: ")
        shift = int(shift)
        
        print(encrypt(msg,shift))
    
    elif val == "2":
        encrypted = input("Encrypted: ")
        shift = input("Shift (leave blank if you don't know): ")
        
        if shift == "":
            decrypt(encrypted)
            
        else:
            decrypt(encrypted, shift)

    else:
        print("That is not an option")


def shift_valid(shift):
    return shift >= 0 & shift <=25 




def encrypt(msg, shift):

    answer = ""

    for i in range(len(msg)):
        
        char = msg[i]
            
        if char.isalnum():        
            if (char.isupper):
                    #ord gets the ascii code of a character
                answer += chr((ord(char)+ shift-65)% 26 +65)

            else:
                answer += chr((ord(char)+ shift-97)% 26 +97)
        else:
            answer+=char

    return answer

def decrypt(encrypted, shift):
    return "placeholder2"


def decrypt(encrypted):
    # Bruteforce the message by testing all possible shifts
    return "placeholder3"




#menu()

# x = encrypt("FLAG{ATTACK}",4)

#EXXEGO

char = 'E'
shift = 4
x = chr((ord(char)+ 26-shift-65)% 26 +65)
print(x)

