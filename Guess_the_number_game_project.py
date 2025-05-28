import random

number = random.randint(1, 100)



def guess_check():

    n = int(input("Enter Your Guess: "))

    if n < number:
        print("Your Guess Is Smaller Than The Number!")

    elif n > number:
        print("Your Guess Is Larger Than The Number!")

    else:
        print("You Guessed The Number Right!")

def attemps():
    i = 0 
    while i < 5:
        guess_check()
        i +=1
    print("Attempts Over Sorry!!")

attemps()


print(number)