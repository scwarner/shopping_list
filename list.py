import os

# make a list to hold onto items
shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# show function to print out list
def show():
    clear_screen()
    print("Here is your list: ")
    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1
    print("-" * 10)

 # print out instructions on how to use app
def help():    
    clear_screen()  
    print("What should we pick up at the store?")  
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' to see instructions.
Enter 'SHOW' to see current list.
Enter 'REMOVE' to delete item from list.
""")

# add new items
def add_to_list(new_item):
    show()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                        "Press ENTER to add to the end of the list\n"
                        "> ".format(new_item))
    else:
        position = 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None 
    if position is not None:
        shopping_list.insert(position-1, new_item)
    else:    
        shopping_list.append(new_item)   
    
    show()
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

def remove_item():
    show()
    what_to_remove = input("What do you want to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show()

help()

# ask for new items
while True:
    new_item = input("> ")
    # quit the app
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        help()
        continue    
    elif new_item.upper() == "SHOW":
        show()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_item()
        continue
    else:  
        add_to_list(new_item)

show()