# Cipher 2.0
# Encrypt function ek message input leta hai aur firr uss message ko encrypt karta hai. 
# Encrypt karne ke liye yeh har character ko 3 character aage wale character se change kar deta hai. 
# Aisa karne ke liye yeh har character ki ascii value ko 3 se increase kar deta hai. 
# Jaise: v ki ASCII value 118 hai, agar hum isse 3 se increase kar de tab yeh 121 ho jayegi. 
# Jo ki 'y' ki ascii value hai. ASCII value nikalne ke liye hum ord() ka use karte hai. 
# Aur ascii value ko string mei convert karne ke liye chr function ka use karte hai. 
# Jaise:

ascii_value = ord("b")+3 # 118
print(ascii_value)
string_value = chr(ascii_value) # v
print(string_value)
 
# Decrypt function encrypt function ka ultaa hai. 
# Yeh value ko 3 se incresae karne ki jagah 3 se kam kar deta hai. 
# Topics covered 
# semantic/syntactic problems in if/else
# problems in while loop
# def encrypt(message):
#     encrypt_message=""
#     message=list(message)
#     for i in message:
#         ascii_message = [ord(char)+3 for char in message]
#         encrypt_message = [ chr(char) for char in ascii_message]  
#     print (''.join(encrypt_message))

# def decrypt():
#   ascii_message = [ord(char) for char in message]
#   decrypt_message = [ chr(char) for char in ascii_message]  
#   print (''.join(decrypt_message))

# flag = True
# while flag == True:
#     choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter 'e' or 'd' respectively!:\n")
#     message = input("Enter your message:\n")
#     if choice == 'e':
#         encrypt(message)
#         play_again = input("Do you want to try agian?(y/n):\n")
#         if play_again == 'y':
#             continue
#         else:
#             break
#     elif choice == 'd':
#         decrypt(message)    
#         play_again = input("Do you want to play again? (y/n)")
#         if play_again == 'y':
#             continue
#         else:
#             break