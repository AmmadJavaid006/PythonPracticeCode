fname = input("Enter File Name: ")
fhandle = open(fname)
lst = list()
count = dict()
finallist = list()
for line in fhandle:
    if line.startswith("From") and not line.startswith("From:"):
        line = line.split()
        lst.append(line[5])

for hour in lst:
    hour = hour.split(":")
    finallist.append(hour[0])
    count[hour[0]] = count.get(hour[0], 0) + 1

for x, y in sorted(count.items()):
    print(x, y)


#################### Can Also Be Written As ####################

fname = input("Enter File Name: ")
fhandle = open(fname)
lst2 = list()
count2 = dict()
for linee in fhandle:
    if linee.startswith("From") and not linee.startswith("From:"):
        linee = linee.split()
        linee = linee[5]
        lst2 = linee[0 : 2]
        count2[lst2] = count2.get(lst2, 0) + 1

for x, y in sorted(count2.items()):
    print(x, y)
