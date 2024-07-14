import re
count = 0
count2 = 0
count3 = 0
count4 = 0

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
    if re.search("^From", line) and not re.search("^From:", line): # Finds line that Starts with 'From' and not with 'From:'
        print(line)
        count2 += 1
print(count2)

################################### Another type of Expression ###################################

fname = input("Enter File Name: ")
fhandle = open(fname)
for line in fhandle:
    if re.search("^X.*:", line): # Starts with 'X' matches any chracter 0 or more times and ':'
        print(line)
        count3 += 1
print(count3)

################################### Another type of Expression ###################################

fname = input("Enter File Name: ")
fhandle = open(fname)
for line in fhandle: 
    if re.search(r"^X-\S+:", line): # Starts with 'X' no WhiteSpace '(" ")' and ':', "r" threats the string like raw string
        print(line)
        count4 += 1
print(count4)