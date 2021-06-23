# Task 1
# for x in range(10):
#     print("Hello")
# Task 2
names = [] #starts with an empty list



for name in range(5): # Can be varied depending on how many names are wanted on the list
    name = input("enter a name " ) #requires user input to enter in a name
    names.append(name) # adds the user input into the list
print(names) # will show all user input in the new updated list

list_names_lower = []
for name in names:
    list_names_lower.append(name.lower())
print(list_names_lower)

for length in names:
    if len(names) % 2 == 0:
        print(f"{names} is even")
    else:
        print(f"{names} is odd")