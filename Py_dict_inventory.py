inventory = {
    
    "Torch": 4,
    "Sticks": 9,
    "Coal": 5,
    "Aid": 5,
    "Water Bottle": 3,
    "Food Rations": 7,
    "Rope": 10
}

addtoinven = [ "Aid", "Water Bottle", "Rope", "Torch", "Coal", "Coal", "Coal", "Coal", "Burner"]


def addtoinventory(inv, invent):
    for x in invent:
        inv[x] = inv.get(x, 0) + 1

addtoinventory(inventory, addtoinven)

def inventorydis(inven):
    print("Inventory")
    count = 0
    for k, v in inven.items():
        print(k, v)
        count += v
    print("Total Items in Inventory are", count)

inventorydis(inventory)
