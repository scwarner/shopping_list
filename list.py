# make a list to hold onto items
shopping_list = []
# show function to print out list
def show():
    print("Here is your list: ")
    for item in shopping_list:
        print(item)

def help():        
    # print out instructions on how to use app
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' to see instructions.
Enter 'SHOW' to see current list.
""")

def add_to_list(new_item):
    # add new items
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

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
    add_to_list(new_item)

show()