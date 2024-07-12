dict = dict()
names = ['csev', 'cwen', 'cwen', 'csev', 'x', 'x', 'x', 'cwen']

for name in names:
    if name not in dict:
        dict[name] = 1
    else:
        dict[name] = dict[name] + 1

print(dict)