import random

highest = 10
answer = random.randint(1, highest)
print(answer) #TODO: Remove after
guess = 0 #Initialise to any number that doesn't answer
print("Please guess the number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

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
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, wrong guess.")


