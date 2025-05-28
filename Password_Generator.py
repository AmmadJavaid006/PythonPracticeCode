import random
import string

x = ""
charval = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

""" for i in range(20):
    password += random.choice(charval) """

list = [random.choice(charval) for i in range(20)]

list_method = "".join([random.choice(charval) for i in range(20)])

######################################################OR######################################################

for i in list:
    x += i

print("Your Random Generated Password is: " + x )
print("Your Random Generated Password is: " + list_method )