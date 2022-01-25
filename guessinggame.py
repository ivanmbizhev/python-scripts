import random


def get_integer(prompt):
    """
    Gets an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The string that the user wil see, when
    they're prompted to enter the value.

    :return: The integer that the user enters. 
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

help(get_integer)

highest = 10
answer = random.randint(1, highest)
print(answer) #TODO: Remove after
guess = 0 #Initialise to any number that doesn't answer
print("Please guess the number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break    
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else: #this must be greater than answer
            print("Please guess lower")




