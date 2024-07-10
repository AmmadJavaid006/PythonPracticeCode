myset = {1, 1, 2, 3, 4, 4, 4, 4, "Hello", "Hello", "World"}

print(myset)
print(type(myset))
print(len(myset))

myset2 = set()
print(type(myset2))
print(myset2)

myset2.add(1)
myset2.add(1)
myset2.add(1)
myset2.add(2)
myset2.add(3)
myset2.add(4)
myset2.add("Hello")
myset2.add("Paa")
myset2.add("Hello")
myset2.add("Hello")

print(myset2)
print(len(myset2))

print("Union " + str(myset.union(myset2)))
print("Intersection " + str(myset.intersection(myset2)))

myset2.remove(4)

print(myset2)
print(str(len(myset2)))

print("Value POPED " + str(myset2.pop()))
print(myset2)

myset2.clear()
print(myset2)