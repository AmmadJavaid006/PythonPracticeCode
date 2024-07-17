end = int(input("Till What Number U Want Sqr: "))
sqrr = [number for number in range(1, end + 1)]
sqr = [sqrnum**2 for sqrnum in sqrr] # =====================> Calculate sqr (**2) of nums
print(sqr)

#########################################################################################

end = int(input("Till What Number U Want All Even Numbers: "))
num = [number for number in range(1, end + 1)]
nums = [int(numz) for numz in num] # ======================== > This line isn't Important
even = [number for number in nums if number % 2 == 0] # ==========> Gives all Even Number
print(even)

#########################################################################################

end = int(input('Till What Number U Want to Replace Even No. with "Even": '))
repeven = ["Even" if number % 2 == 0 else number for number in range(1, end + 1)]
print(repeven) # ==================================> Replaces all Even Number with "Even"

#########################################################################################

end = int(input("Enter Number For Sqr tuple: "))
list = [number for number in range(1, end + 1)]
sqrnum = [(sqrnums, sqrnums**2) for sqrnums in list] # ==> Give a tuple of number and its 
print(sqrnum) # =============================================================> sqr (2, 4)

#########################################################################################

matrix = [[i + z*3 + 1 for i in range(3)] for z in range(3)]
print("Matrix")
for row in matrix:
    print(row, end = " \n") # =====================================> Creates a 3x3 Matrix

#########################################################################################

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatlist = [elements for element in list for elements in element]
print("Flatlist")
print(flatlist) # ============================================> Gives a Flat-List/Filters

#########################################################################################

words = ["apple", "banana", "cherry"]
list = [len(item) for item in words] # =======> Gives the number of character in the word
print("Character")
print(list)

#########################################################################################

sentence = "The quick brown fox jumps over the lazy dog"
list = [len(word) for word in sentence.split()] # ========> Gives the number of character 
print("Character")
print(list) # ================================================================> in a word

#########################################################################################

end = int(input("Enter Number Of Digits: "))
list = [number for number in range(1, end + 1)]
finallist = [number for number in list if number % 3 == 0] # ==========> Gives all number 
print(finallist) # ===========================================>that are divisiable by "3"

#########################################################################################

list = ['a', 'b', 'c', 'd']

tuplelist = [(list.index(index), index) for index in list]
print("Index with Number")
print(tuplelist) # ===============================> Gives tuples with their corresponding  
# ===================================================> Index and value from List (1, 'a')

#########################################################################################

n = int(input("Value for NxN is: "))
matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print("Matrix")
for i in matrix: # ===============> Gives a NxN matrix of numbers with 1 going Diagonally
    print(i)

#########################################################################################

matrix = [[5 * (i * 5 + j + 1) for j in range(5)] for i in range(5)]
print("Matrix")
for z in matrix: # =============================> Gives a 5x5 Matrix with multiples of 5
    print(z, end = ",\n")

#########################################################################################

matrix = [[2 * (i * 5 + j + 1) for j in range(5)] for i in range(5)]
print("Matrix")
for z in matrix:
    print(z, end = " \n")

#########################################################################################

matrix = [[3 * (i * 4 + j + 1) for j in range(4)] for i in range(5)]
print("Matrix")
for z in matrix:
    print(z)

#########################################################################################

n = int(input("Enter Number of Rows: "))
m = int(input("Enter Number of Columns: "))
matrix = [[i * m + z + 1 for z in range(m)] for i in range(n)]
print("Matrix")
for x in matrix:
    print(x)

#########################################################################################

matrix = [[1 if r <= c else 0 for r in range(10)] for c in range(10)]
print("Matrix")
for s in matrix:
    print(s)

#########################################################################################

matrix = [[2 if (i * 5 + z + 1) % 2 == 0 else 1 for z in range(5)] for i in range(5)]
print("Matrix")
for x in matrix:
    print(x)

#########################################################################################

matrix = [[1 if r >= c else 0 for r in range(10)] for c in range(10)]
print("Matrix")
for s in matrix:
    print(s)

#########################################################################################

list = [i for i in range(1, 8)]
matrix = [[(i + j) % 2 for j in range(8)] for i in range(8)]
print("Matrix")
for x in matrix:
    print(x)