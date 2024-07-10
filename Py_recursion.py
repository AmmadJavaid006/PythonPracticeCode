import random
print("Countdown Sequence")
n = int(input("Starting Number: "))

def count(n):
    
    if n == 0:
        return
    print(n)
    count(n - 1)

count(n)

print("Factorial Sequence")
factno = int(input("Number of Digits for Factorial: "))

def fact(factno):
    
    if factno == 1 or factno == 0:
        return 1
    
    else:
        return fact(factno - 1) * factno

print(fact(factno))

print("Sum Sequence")
ntn = int(input("Enter number of digits for sum: "))

def calc_sum(ntn):

    if ntn == 0:
        return 0
    return calc_sum(ntn - 1) + ntn

print(calc_sum(ntn))

import random
print("List Sequence")
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


def el_prt(list, idx = 0):

    if idx == len(list):
        return
    print(list[idx])
    el_prt(list, idx + 1)

print(el_prt(list))
