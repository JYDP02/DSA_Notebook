# Function for Ciphering the message
def caesar_cipher(message, key):
    ciphered_message = ""
    # Loop to get each character of the message
    for index in range(len(message)):
        character = message[index]  # current character stored

        # if its a space, character not updated
        if character == ' ':
            ciphered_message += character
            continue

        # we add to ciphered message the character that is present after moving forward key times
        if character.isupper():
            ciphered_message += chr((ord(character) + key - 65) % 26 + 65)  # in respect to Ascii value of A
        else:
            ciphered_message += chr((ord(character) + key - 97) % 26 + 97)  # in respect to Ascii value of a

    return ciphered_message

# Function for Deciphering the message
def caesar_decipher(message, key):
    deciphered_message = ""
    # Loop to get each character of the message
    for index in range(len(message)):
        character = message[index]  # current character stored

        # if its a space, character not updated
        if character == ' ':
            deciphered_message += character
            continue

        # we add to ciphered message the character that is present after moving backward key times
        if character.isupper():
            deciphered_message += chr((ord(character) - key - 65) % 26 + 65)  # in respect to Ascii value of A
        else:
            deciphered_message += chr((ord(character) - key - 97) % 26 + 97)  # in respect to Ascii value of a

    return deciphered_message


print("Press '1' for ciphering. \nPress '2' for deciphering.")
t = input("Enter choice : ")

if t == "1":
    message = input("Enter message to cipher : ")
    key = int(input("Enter key value : "))

    cipher_message = caesar_cipher(message, key)
    print("Ciphered Message : "+cipher_message+"\n")

if t == "2":
    message = input("Enter message to decipher : ")
    key = int(input("Enter key value : "))

    deciphered_message = caesar_decipher(message, key)
    print("Deciphered Message : "+deciphered_message+"\n")


'''
Input description: 
    Line 1 -- Choice as 1 or 2 for ciphering and deciphering respectively
    Line 2 -- Message to cipher/decipher
    Line 3 -- Key to cipher/decipher
     
Output Description :
    Ciphered Message : Ciphered_Message
        or
    Deciphered Message : Deciphered_Message
    
Example Outputs:

Input 1:
    Press '1' for ciphering. 
    Press '2' for deciphering.
    Enter choice : 1
    Enter message to cipher : Hello World
    Enter key value : 5
Output 1:
    Ciphered Message : Mjqqt Btwqi
    
Input 2:
    Press '1' for ciphering. 
    Press '2' for deciphering.
    Enter choice : 2
    Enter message to decipher : Mjqqt Btwqi
    Enter key value : 5
Output 2:
    Deciphered Message : Hello World

'''