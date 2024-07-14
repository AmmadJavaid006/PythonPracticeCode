import re

x = "My 4 fav nums are 42, 65, 89 and 55"
num = re.findall("[0-9]+", x) # find all numbers ranging from 0-9 and they can be 1 or more
print(num)

########################## Another Example ##########################

vowels = re.findall("[AEIOU]+", x) # find all vowels
print(vowels) # ======> will return an empty string bcz no element matches

########################## Applying x.upper() ##########################

vowels = re.findall("[AEIOU]+", x.upper()) # find all vowels
print(vowels) # ======> This time it will return list of ['A', 'U', 'A', 'E', 'A'] 
# ====================> Bcz x.upper() makes the string all uper case and [AEIOU]+ matches

########################## Greedy and Non-Greedy Expressions ##########################

# Greedy
sen = "From: using the: Character"
senf = re.findall("^F.+:", sen) # =========> "^F.+:" this is a greedy expression it will go as far as it can
print(senf) # =============================> and will stop at the ":" before 'the'

# Non-Greedy
sen = "From: using the: Character"
senf = re.findall("^F.+?:", sen) # =========> "^F.+?:" this is a non-greedy expression it will go till it finds
print(senf) # =============================> the first ":" that is after 'From'

########################## Adding Paranthasis ##########################

addr = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
addrf = re.findall(r"\S+@\S+", addr) # ========> Finds the first "Non-WhiteSpace" goes till at then finds another
print(addrf) # ================================> another "Non-WhiteSpace" and then ends

########################## Adding Paranthasis ##########################

addr = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
addrf = re.findall(r"@(\S+)", addr) # ========> Finds the @ and starts from next character and end 
print(addrf) # =================================> WhiteSpace Comes

########################## Making It Match More ##########################

addr = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
addrf = re.findall(r"^From .*@(\S+)", addr) # ========> Finds the Starting From and then @ and starts from  
print(addrf) # =================================> next character and end WhiteSpace Comes