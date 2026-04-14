# Create a program that saves a shopping list. It should ask the user which item they want to add to the list.
# If they type just 'q', the program should stop adding to the list.
# After that, all the items added should be printed on the screen, as well as the quantity of items.
# You have a son who likes to give different names to items on the shopping list.
# After the list is created, ask the user to give special names to some items.
# To stop asking, they should type 'q'.
# When printing, place the "special" name next to the item, if there is one.

shopping_list = []
print('---- Shopping List ---- ')

while True:
    item = input('Enter the item to add to your list: (or "q" to stop) ')  
    if item == 'q':
        break
    shopping_list.append(item)

print()
print('---- Current List ----')
for i in shopping_list:
    print(f"{i}", end=', ')
print()

renamed_items = {}

print('\nWould you like to rename any items? (y/n) ')
special = input()

if special == 'y':
    while True:
        print('Which item would you like to rename? (or "q" to stop)')
        to_rename = input()
        
        if to_rename == 'q':
            break
        
        if to_rename in shopping_list:
            new_name = input('Enter the new name: ')
            renamed_items[to_rename] = new_name
        else:
            print("That item is not in the list!")

print('\n---- New List ----')
for i in shopping_list:
    if i in renamed_items:
        nickname = renamed_items[i]
        print(f"{i} ({nickname} special)")
    else:
        print(f"{i}")