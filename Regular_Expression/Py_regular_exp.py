import re
count = 0
count2 = 0

fname = input("Enter File Name: ")
fhandle = open(fname)
for line in fhandle:
    if line.startswith("From") and not line.startswith("From:"):
        print(line)
        count += 1
print(count)

################################### Both Are Same ###################################

fname = input("Enter File Name: ")
fhandle = open(fname)
for line in fhandle:
    if re.search("^From", line) and not re.search("^From:", line):
        print(line)
        count2 += 1
print(count2)
