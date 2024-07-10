import random, sys

list = []
n = random.randint(1, 7)

if n == 1:
    print("Total Elements '1'")
    e1 = input("Enter Elements 1: ")
    list.append(e1)

elif n == 2:
    print("Total Elements '2'")
    e1 = input("Enter Elements 1: ")
    e2 = input("Enter Elements 2: ")
    list.append(e1)
    list.append(e2)

elif n == 3:
    print("Total Elements '3'")
    e1 = input("Enter Elements 1: ")
    e2 = input("Enter Elements 2: ")
    e3 = input("Enter Elements 3: ")
    list.append(e1)
    list.append(e2)
    list.append(e3)

elif n == 4:
    print("Total Elements '4'")
    e1 = input("Enter Elements 1: ")
    e2 = input("Enter Elements 2: ")
    e3 = input("Enter Elements 3: ")
    e4 = input("Enter Elements 4: ")
    list.append(e1)
    list.append(e2)
    list.append(e3)
    list.append(e4)

elif n == 5:
    print("Total Elements '5'")
    e1 = input("Enter Elements 1: ")
    e2 = input("Enter Elements 2: ")
    e3 = input("Enter Elements 3: ")
    e4 = input("Enter Elements 4: ")
    e5 = input("Enter Elements 5: ")
    list.append(e1)
    list.append(e2)
    list.append(e3)
    list.append(e4)
    list.append(e5)

elif n == 6:
    print("Total Elements '6'")
    e1 = input("Enter Elements 1: ")
    e2 = input("Enter Elements 2: ")
    e3 = input("Enter Elements 3: ")
    e4 = input("Enter Elements 4: ")
    e5 = input("Enter Elements 5: ")
    e6 = input("Enter Elements 6: ")
    list.append(e1)
    list.append(e2)
    list.append(e3)
    list.append(e4)
    list.append(e5)
    list.append(e6)


def elementcount(list):

    elementcount = len(list)
    print("Number of Elements in this list are", elementcount)

def elementsinlist(list):
    
    for i in list:
        print(i + ",", end = " " )

elementcount(list)
elementsinlist(list)

nfact = int(input("\nEnter Number of Digits for Factorial: "))


def factorial(nfact):

    fact = 1
    for x in range(1, nfact+1):
       fact *= x
    print("Factorial is:", fact)

factorial(nfact)






