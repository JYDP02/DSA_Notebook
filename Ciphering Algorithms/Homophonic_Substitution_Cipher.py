import random # need random module to generate choices in key

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # string with all alphabets


# Function for Ciphering the message
def homophonic_substitution_cipher(message, key):

    # making cipher key
    cipher_key = [] # List for storing ciphering key
    cipher_key_choices = "" # string for ciphering key of individual characters

    # Loop for creating the cipher key
    for index in range(len(key)):
        if key[index] == ' ':
            # if character is space , then the keys for current character is saved in cipher key list
            cipher_key.append(cipher_key_choices)
            cipher_key_choices = ""  # the string is emptied for storing next character's keys
            continue

        cipher_key_choices += key[index] # else the key choices for current character are stored in string
        if index == len(key) - 1:
            # if no space is encoutered and the its the last character then the key choices are added to the list
            cipher_key.append(cipher_key_choices)

    # Creating the ciphered message
    ciphered_message = ""  # string to store the ciphered message
    for character in message:
        # Looping through all the characters in message
        if character in characters:
            # if character is an alphabet, we are generating a random character
            # from the cipher key choices respective to this character and adding it to the ciphered message
            character_key_choices = list(cipher_key[characters.find(character)])
            ciphered_message += random.choice(character_key_choices)
        else:
            # else we will be adding directly the current character as its not one of the alphabets
            ciphered_message += character

    return ciphered_message


def homophonic_substitution_decipher(message, key):

    # making cipher key
    cipher_key = []  # List for storing ciphering key
    cipher_key_choices = ""  # string for ciphering key of individual characters

    # Loop for creating the cipher key
    for index in range(len(key)):
        if key[index] == ' ':
            # if character is space , then the keys for current character is saved in cipher key list
            cipher_key.append(cipher_key_choices)
            cipher_key_choices = ""  # the string is emptied for storing next character's keys
            continue

        cipher_key_choices += key[index]  # else the key choices for current character are stored in string
        if index == len(key) - 1:
            # if no space is encountered and the its the last character then the key choices are added to the list
            cipher_key.append(cipher_key_choices)

    # Creating the deciphered message
    deciphered_message = ""  # string to store the ciphered message
    for character in message:
        # Looping through to get all characters in ciphered message
        if character == ' ':
            # if character is a space, adding it directly to the deciphered message
            deciphered_message += character
            continue

        # else looping through the cipher key
        for index in range(len(cipher_key)):
            # storing the key choices for individual characters
            character_key_choices = list(cipher_key[index])

            # if the current character in ciphered message belong to any one of the characters
            # in list of the cipher key choices for some particular character while looping
            # then adding that current character to deciphered message
            if character in character_key_choices:
                deciphered_message += characters[index]

    return deciphered_message


# Driver Code
print("Press '1' for ciphering. \nPress '2' for deciphering.")
t = input("Enter choice : ")

if t == "1":
    message = input("Enter message to cipher : ")
    key = list(input("Enter space seperated key for 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' : "))

    ciphered_message = homophonic_substitution_cipher(message, key)
    print("Ciphered Message : " + ciphered_message + "\n")

if t == "2":
    message = input("Enter message to decipher : ")
    key = list(input("Enter space seperated key for 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' : "))

    deciphered_message = homophonic_substitution_decipher(message, key)
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
    Enter space seperated key for 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' : D2 E3 F G H I78 J M L45 K1 N0 O P Q 6R S T U9 W X Y A Z B C V

Output 1:
    Ciphered Message : MHOO6

Input 2:
    Press '1' for ciphering. 
    Press '2' for deciphering.
    Enter choice : 2
    Enter message to decipher : MHOO6
    Enter space seperated key for 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' : D2 E3 F G H I78 J M L45 K1 N0 O P Q 6R S T U9 W X Y A Z B C V
    
Output 2:
    Deciphered Message : HELLO
'''