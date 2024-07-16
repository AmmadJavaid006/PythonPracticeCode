""" end = int(input("Till What Number U Want Sqr: "))
sqrr = [number for number in range(1, end + 1)]
sqr = [sqrnum**2 for sqrnum in sqrr] # Calculate sqr (**2) of nums
print(sqr) """

#########################################################################################

""" end = int(input("Till What Number U Want All Even Numbers: "))
num = [number for number in range(1, end + 1)]
nums = [int(numz) for numz in num]
even = [number for number in nums if number % 2 == 0]
print(even) """

#########################################################################################

""" end = int(input('Till What Number U Want to Replace Even No. with "Even": '))
repeven = ["Even" if number % 2 == 0 else number for number in range(1, end + 1)]
print(repeven) """

#########################################################################################

""" end = int(input("Enter: "))
list = [number for number in range(1, end + 1)]
sqrnum = [(sqrnums, sqrnums**2) for sqrnums in list]
print(sqrnum) """

#########################################################################################

""" finallist = [[i + z*3 + 1 for i in range(3)] for z in range(3)]
for row in finallist:
    print(row, end = ",\n") """

#########################################################################################

""" list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatlist = [elements for element in list for elements in element]
print(flatlist) """

#########################################################################################

""" words = ["apple", "banana", "cherry"]
list = [len(item) for item in words] 
print(list) """

#########################################################################################

""" sentence = "The quick brown fox jumps over the lazy dog"
list = [len(word) for word in sentence.split()]
print(list) """

#########################################################################################

""" end = int(input("Enter Number Of Digits: "))
list = [number for number in range(1, end + 1)]
finallist = [number for number in list if number % 3 == 0]
print(finallist) """

#########################################################################################

""" list = ['a', 'b', 'c', 'd']

tuplelist = [(list.index(index), index) for index in list]
print(tuplelist) """

#########################################################################################

""" n = int(input("Value for NxN is: "))
matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
for i in matrix:
    print(i) """

#########################################################################################

matrix = [[5 * (i * 5 + j + 1) for j in range(5)] for i in range(5)]
for z in matrix:
    print(z, end = ",\n")
