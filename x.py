from random import sample, shuffle

digits = 3
guesses = 10

print('I am thinking of a', digits, 'digit number.')
print('Try to guess what it is.')
print('Here are some clues:')
print('When I say:    That means:')
print('  pico         One digit is correct but in the wrong position.')
print('  fermi        One digit is correct and in the right position.')
print('  bagels       No digit is correct.')
print('There are no repeated digits in the number.')

# Create a random number.

letters = sample('0123456789', digits)

if letters[0] == '0':
    letters.reverse()

number = ''.join(letters)

print('I have thought up a number.')
print('You have', guesses, 'guesses to get it.')

counter = 1

while True:
    print('Guess #', counter)
    guess = input()

    if len(guess) != digits:
        print('Wrong number of digits. Try again!')
        continue

    # Create the clues.

    clues = []

    for index in range(digits):
        if guess[index] == number[index]:
            clues.append('fermi')
        elif guess[index] in number:
            clues.append('pico')

    shuffle(clues)

    if len(clues) == 0:
        print('bagels')
    else:
        print(' '.join(clues))

    counter += 1

    if guess == number:
        print('You got it!')
        break

    if counter > guesses:
        print('You ran out of guesses. The answer was', number)
        break




























#sample
# Syntax
# random.sample(sequence, k)
#sample refers to the list or range or set or dictionary any iterable object.i.e it should be a sequence data type
#k refers to the length of the returned list of random elements or the number of elements you want in return

#Example:
#code:
# import random
# mylist = ["apple", "banana", "cherry"]
# print(random.sample(mylist, k=2))
#output:
# any combination of two elements of thw list:
# for eg="apple","cherry" or "apple","banana"

#######################################################################################################

#join
# Syntax
# string.join(iterable)
#string refers to anything by which you want to join the elements
#iterable refers to any object where the values returned will be in string

#Example:
#code:
# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x)
#output:
# John#Peter#Vicky

###########################################################################################################

#shuffle
#Syntax
# random.shuffle(sequence, function)
#sequence refers to a sequence.
#function refers to the name of a function that returns a number between 0.0 and 1.0.
#If not specified, the function random() will be used

#Example
#code:
# Shuffle a list (reorganize the order of the list items):
# import random
# mylist = ["apple", "banana", "cherry"]
# random.shuffle(mylist)
# print(mylist)
#output:
# any possible shuffle combination:
# for eg:['apple', 'cherry', 'banana']
# The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
# Note: This method changes the original list, it does not return a new list.

#############################################################################################################

#strip
# Syntax
# string.strip(characters)
#string refers to the sequence or string from with you want to remove the mentioned character or string
#character refers to anything you want to remove from the whole string

#Example:
#code:
# Remove spaces at the beginning and at the end of the string:
# txt = "     banana     "
# x = txt.strip()
# print("of all fruits", x, "is my favorite")
#output:
# of all fruits banana is my favorite
# The strip() method removes any leading (spaces at the beginning) and 
# trailing (spaces at the end) characters (space is the default leading character to remove)

#Example2
#code:
# Remove the leading and trailing characters:
# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x)
#output:
# banana