import sys

list = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49
idx = 0

for i in list:
    if (i == x):
        print("Found 'X' at INDEX " + "'" + str(idx) + "'" )
    idx += 1
        
