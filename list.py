# make a list to hold onto items
shopping_list = []
# print out instructions on how to use app
print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")
# ask for new items
while True:
    new_item = input("> ")
    # quit the app
    if new_item == 'DONE':
        break
# add new items
    shopping_list.append(new_item)
#print out list
print("Here is your list: ")
for item in shopping_list:
    print(item)