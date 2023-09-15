import os as os
#os.system('cls')
# This cleans up the terminal a little bit. It's a habit I picked up from using MATLAB. I would like your feedback on this practice.


shop = ['Subway','St. Louis','Missouri']

pins = {12: 'Danielle', 104: 'Anya', 69: 'Michelle', 75: 'Ethan'}

print(shop)

InputCode = input("Please enter your PIN code: ")
InputCode = int(InputCode)

if InputCode in pins:
    #print('reeee')
    query = input('What can I find for you?')
    myFile = open("c:/Users/store/OneDrive/Documents/Senior Year/Python/inventory.txt", "r")
    #print(myFile)
    items = (myFile.read())
    #print(items)
    items = items.splitlines()
    #print(items)
    findInStore = lambda query : f"{query} is stocked" if query in items else f"{query} is not in stock"
    Cheeseburger = findInStore(query)
    print(Cheeseburger)

else:
    print('This PIN is not in the database. Authorized users are:')
    for items, ungabunga in pins.items():
        print(ungabunga)
    


