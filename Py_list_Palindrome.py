mylist1 = [1, 2, 3, 2, 1]
mylist2 = [1, "abc", "abc", 1]

mylist1clone = mylist1.copy()
mylist1clone.reverse()

mylist2clone = mylist2.copy()
mylist2clone.reverse()

if mylist1clone == mylist1:
    print(str(mylist1) + " " + str(mylist1clone) + " Are Palindromes")

if mylist2clone == mylist2:
    print(str(mylist2) + " " + str(mylist2clone) + " Are Palindromes")

if mylist1 != mylist1clone and mylist2 != mylist2clone:
    print("Both are NOT A PALINDROME")

elif mylist1 != mylist1clone:
    print("mylist1 and mylist1clone are NOT A PALINDROMES")

elif mylist2 != mylist2clone:
    print("mylist2 and mylist2clone are NOT A PALINDROMES")