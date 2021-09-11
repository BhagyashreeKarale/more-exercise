# Cipher 1.0
# Apne simple se message ko aise change karna jisse koi dusra insaan usse samajh na paye 
# usse encryption bolte hai. 
# Encryption karne ke bhot sare ways hote hai. Hum cipher wheel use karenge. 
# Cipher wheel mei hum her character ko kissi number se aage shift kar dete hai. 
# Jaise: Hum iss cihper wheel mein her character ki value ko 2 se increase kar denge. 
# Aisa karne ke liye hum chars aur shifted_chars array ka use karenge. Example:

chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
 
# # Topics covered * 
# # function returning the wrong value
# # argument passed to the function but never used.
# # for loop itterates over wrong string
# # semantic/syntactic problems in if/else
# # Neeche yeh program diya hua hai, isko sahi kar ke ek nayi file mein submit karo.

# Cipher wheel with a function for finding an element in a list

# find_in_list function defined here but not called
def find_in_list(query, mainlist):
# this function is used to find the position of the "query" in the "mainlist". If "query" is in the list then it returns its position, otherwise it returns None
    mainlist_len = len(mainlist)
    range_for_loop = range(mainlist_len)
    index = None
    for i in range_for_loop:
        element = mainlist[i]
        if element == query:
            index = i
            return i
# this should return the position of the "query" in the "mainlist"


chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

# encrypt_message function defined here but not called
def encrypt_message(plain_msg):
# this fucnction takes "plain_msg" as an argument and print/return the encrypted message. The "plain_msg" is tranfered into "encrypted_msg" using "shifted_chars" list. Example, if plain_msg = "ng" then n => p, g => i  and hence encrypted_msg = "pi"
    encrypted_msg = ""
    for character in plain_msg:
      # for character in msg
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char
        else:
            encrypted_msg = encrypted_msg + character
    print("Your encrypted message :",encrypted_msg)
    return encrypted_msg

# decrypt_message function defined here but not called
def decrypt_message(encrypted_msg):
# this fucnction takes "encrypted_msg" as an argument and print/return the encrypted message. The "encrypted_msg" is tranfered into "decrypted_msg" using "shifted_chars" list. Example, if encrypted_msg = "pi" then p => n, i => g  and hence decrypted_msg = "ng"
    decrypted_msg = ""
    for character in encrypted_msg:
        if character in shifted_chars:
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            decrypted_msg = decrypted_msg + new_char
        else:
            decrypted_msg = decrypted_msg + character
    print("Your decrypted message : ",decrypted_msg)
    return decrypted_msg


# methods should return or print the new messages.
############################################### Code starts from here ##################################################
flag = True
while flag == True:
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message \nEnter `e` or `d` respectively!:\n")
    if choice == 'e':
        plain_message = input("Enter message to encrypt :\n")
        encrypt_message(plain_message)
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N):\n")
        if play_again == 'Y' or play_again == "y":
            continue
        elif play_again == 'N' or play_again == "n":
            print("Hope to see you soon!Good bye:)")
            break
    elif choice == 'd':
        encrypted_msg = input("Enter message to decrypt :\n")
        decrypt_message(encrypted_msg)
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N):\n")
        if play_again == 'Y' or play_again == "y":
            continue
        elif play_again == 'N' or play_again == "n":
            print("Hope to see you soon!Good bye:)")
            break











##################################################################################################################
#this function is just to find the index number of the respective letter in tha mainlist.i.e the char list
# def find_in_list(query, mainlist):
#     for i in range(len(mainlist)):
#         if mainlist[i] == query:
#             return i
# chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
#                  'v','w','x','y','z']
# shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
#                  'x','y','z','a','b']
# #in this function we are going the encrypt the msg by replacing the character by the character present at the same index number but i shifted chars list
# def encrypt_message(plain_msg):
#     plain_msg=list(plain_msg)
#     encrypted_msg = ""
#     for character in plain_msg:
#         if character in chars:
#             char_index = find_in_list(character, chars)
#             new_char = shifted_chars[char_index]
#             encrypted_msg = encrypted_msg + new_char
#         else:
#             encrypted_msg = encrypted_msg + character
#     print( encrypted_msg )
# #in this function we are going the decrypt the msg by replacing the character by the character present at the same index number but in mainlist list
# def decrypt_message(encrypted_msg):
#     decrypted_msg = ""
#     for character in encrypted_msg:
#         if character in shifted_chars:
#             char_index = find_in_list(character, shifted_chars)
#             new_char = chars[char_index]
#             decrypted_msg = decrypted_msg + new_char
#         else:
#             decrypted_msg = decrypted_msg + character
#     print( decrypted_msg )

# flag = True
# while flag == True:
#     choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!:\n")
#     if choice == 'e':
#         plain_message = input("Enter message to encrypt:\n")
#         encrypt_message(plain_message)
#         play_again = input("Do you want to try agian or Do you want to exit? (Y/N):\n")
#         if play_again == 'Y':
#             continue
#         else:
#             break
#     elif choice == 'd':
#         encrypted_msg = input("Enter message to decrypt:\n")
#         decrypt_message(encrypted_msg)
#         play_again = input("Do you want to try agian or Do you want to exit? (Y/N):\n")
#         if play_again == 'Y':
#             continue
#         else:
#             break
#     else:
#         print("Enter valid input!")
