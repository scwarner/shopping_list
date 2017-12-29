# make a list to hold onto items
shopping_list = []

# show function to print out list
def show():
    print("Here is your list: ")
    for item in shopping_list:
        print(item)

 # print out instructions on how to use app
def help():        
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' to see instructions.
Enter 'SHOW' to see current list.
Enter 'REMOVE' to delete last item from list.
""")

# add new items
def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

def remove_item():
    print("Say 'goodbye' to {}.".format(shopping_list[-1]))
    shopping_list.pop(-1)

print("What should we pick up at the store?")
help()

# ask for new items
while True:
    new_item = input("> ")
    # quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        help()
        continue    
    elif new_item == "SHOW":
        show()
        continue
    elif new_item[0] == "s":
        print("Sorry, you can't have that.")
        continue  
    elif new_item == 'REMOVE':
        remove_item()
        continue     
    add_to_list(new_item)

show()