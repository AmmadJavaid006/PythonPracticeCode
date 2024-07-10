n = int(input("Number of Natural digits for the sum are: "))
i = 0
z = 1
sum = 0
factorial = 1

while i <= n:
    sum += i
    i += 1
print("Total = ", sum)

print("Time for Factorials...")
f = int(input("Number of Natural digits for the factorials are: "))

while z <= f:
    factorial *= z
    z += 1
print("Factorial = ", factorial)