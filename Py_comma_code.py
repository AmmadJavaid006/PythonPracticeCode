""" 
def commaCode():
    items = []
    while True:
        print('Enter an item (Or enter nothing to stop):')
        name = input()
        if name == '':
            break
        items = items + [name]
    print('Items are:')
    for name in items:
        
        if items.index(name) == (len(items) - 2 ):
            print("and")
        elif items.index(name) == (len(items) - 1):
            print(name)
        else:
            print(name, end= ", ")


commaCode() """

t = [9, 41, 12, 3, 74, 15]
print(t[12 : 3])