n = int(input("Number of Natural digits for the sum are: "))
sum = 0
factorial = 1

for i in range(1, n+1):
    sum += i 
print("Sum = ", sum) 

print("Time for Factorials...")
f = int(input("Number of Natural digits for the factorials are: "))

for z in range(1, f+1):
    factorial *= z
print("Factorial = ", factorial)