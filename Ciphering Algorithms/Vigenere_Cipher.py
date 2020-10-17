# Function for Ciphering the message
def vigener_cipher(message, key):
    cipher_key = "" # string to store the ciphering key
    index = 0
    # creating the ciphering key
    while len(cipher_key) != len(message): # loop to generate repeated key upto length of message
        cipher_key += key[index] # adding key charactes to ciphering key
        if index == len(key) - 1:
            # if length of message is not reached and the key is inserted
            # we repeat it until length of message is reached
            index = 0
            continue
        index += 1  # incrementing the index

    ciphered_message = "" # string to store the ciphered message
    for index in range(len(message)):
        # loop to go through all characters in message

        message_character = ((ord(message[index]) + ord(cipher_key[index])) % 26) + ord('A')
        # storing the character got from modifying message character with ciphering key

        ciphered_message += chr(message_character) # adding message charater to ciphered message

    return ciphered_message


# Function for Deciphering the message
def vigenere_decipher(message, key):
    cipher_key = ""  # string to store the ciphering key
    index = 0
    while len(cipher_key) != len(message):  # loop to generate repeated key upto length of message
        cipher_key += key[index]  # adding key characters to ciphering key
        if index == len(key) - 1:
            # if length of message is not reached and the key is inserted
            # we repeat it until length of message is reached
            index = 0
            continue
        index += 1  # incrementing the index

    deciphered_message = ""  # string to store the deciphered message
    for index in range(len(message)):
        # loop to go through all characters in message

        message_character = ((ord(message[index]) - ord(cipher_key[index]) + 26) % 26) + ord('A')
        # storing the character got from modifying message character with ciphering key

        deciphered_message += chr(message_character)
        # adding message charater to deciphered message

    return deciphered_message


# Driver Code
print("Press '1' for ciphering. \nPress '2' for deciphering.")
t = input("Enter choice : ")

if t == "1":
    message = input("Enter message to cipher : ")
    key = list(input("Enter key : "))

    ciphered_message = vigener_cipher(message, key)
    print("Ciphered Message : " + ciphered_message + "\n")

if t == "2":
    message = input("Enter message to decipher : ")
    key = list(input("Enter key : "))

    deciphered_message = vigenere_decipher(message, key)
    print("Deciphered Message : " + deciphered_message + "\n")

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
    Enter message to cipher : HELLO
    Enter key : NET

Output 1:
    Ciphered Message : UIEYS


Input 2:
    Press '1' for ciphering. 
    Press '2' for deciphering.
    Enter choice : 2
    Enter message to decipher : UIEYS
    Enter key : NET
    
Output 2:
    Deciphered Message : HELLO

'''