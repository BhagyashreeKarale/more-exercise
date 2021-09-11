# Conditionals, Loop and Variable Naming
# Yeh rock paper scissors game ka program hai. 
# Iss game ko aap computer ke against kheloge. 
# Iss game ke 3 rules hai 
# * Rock Paper se haar jata ha
#   Paper Scissors se haar jaata hai
#   Aur, Scissors Rock se.
# Appko pehle rock,paper ya scissors mei se chose karna hoga. 
# Aur uske baad computer randomly inme se ek option chose karega. 
# Firr, upar diye gaye rules ke hisab se result aayega. 
# Jaise: * Agar aapne "Rock" chose kiya aur computer ne "Scissors"

# To aap jeet jaoge kyunki "Rock" "Scissors" ko hara deta hai. ( Rule 3 )
# Aap iss game ke rules iss


# se seekh sakte hai. Topics covered: * semantic/syntactic problems in if/else

# semantic error in while conditions

# errors in variable naming

import random
def win():
    print ('You win!')
def lose():
    print ('You lose!')
while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    # player_choice.strip()
    # random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(moves)

    if player_choice == computer_choice:
        print ('Draw!')
    elif  player_choice== 'rock' and computer_choice == 'scissors':
        win()
    elif  player_choice == 'paper' and computer_choice == 'scissors':
        lose()
    elif player_choice == 'scissors' and computer_choice == 'paper':
        win()
    elif player_choice == 'scissors' and computer_choice == 'rock':
        lose()
    elif player_choice == 'paper' and computer_choice == 'rock':
        win()
    elif player_choice =="rock"  and computer_choice == "paper":
        lose()
    aGain = input('Do you want to play again? (y or n)').strip()
    if aGain == 'n':
        break