# Encrypt Autokey Cipher Messages

# Ciphering the message using the Autokey method
def autokey_cipher(message, key):
    ciphered_message = ""
    index = 0
    # Generating the key using message
    # Concatenating the message itself after the key upto length of the message
    while len(key) != len(message):
        key += message[index]
        index += 1

    # Generating the ciphered message with the autokey method
    # by mapping each character of the message to each character of key
    for index in range(len(message)):
        character = ((ord(message[index]) + ord(key[index])) % 26) + ord('A')
        ciphered_message += chr(character)

    return ciphered_message


# Deciphering the message using the Autokey method
def autokey_decipher(message, key):
    deciphered_message = ""
    index = 0
    # Generating the key using ciphered message
    # Modifying the message and then concatenating it to the key to get the same key used to cipher
    while len(key) != len(message):
        key += chr(((ord(message[index]) - ord(key[index])) % 26) + ord('A'))
        index += 1

    # Generating the deciphered message with the autokey method
    # by mapping each character of the message to each character of key
    for index in range(len(message)):
        character = ((ord(message[index]) - ord(key[index])) % 26) + ord('A')
        deciphered_message += chr(character)

    return deciphered_message


print("Press '1' for ciphering. \nPress '2' for deciphering.")
t = input("Enter choice : ")

if t == "1":
    message = input("Enter message to cipher : ")
    key = input("Enter key value : ")

    cipher_message = autokey_cipher(message, key)
    print("Ciphered Message : " + cipher_message + "\n")

elif t == "2":
    message = input("Enter message to decipher : ")
    key = input("Enter key value : ")

    deciphered_message = autokey_decipher(message, key)
    print("Deciphered Message : " + deciphered_message + "\n")

else:
    print("Wrong Choice !!!")
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
    Enter message to cipher : HEYTHERE
    Enter key value : S
Output 1:
    Ciphered Message : ZLCRALVV

Input 2:
    Press '1' for ciphering. 
    Press '2' for deciphering.
    Enter choice : 2
    Enter message to decipher : ZLCRALVV
    Enter key value : S
Output 2:
    Deciphered Message : HEYTHERE
'''