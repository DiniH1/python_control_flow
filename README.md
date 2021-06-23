# Control flow wih if, elif, else conditions
## Loops - for loop and while loop
- when do we need to use these conditions?
#Snytax

`weather = "rainy"`


`if weather == "rainy":  # if this condiion is true the next lin will execute
    print("Take an umbrella!") # this line needs to be inside the if code block - indented
elif weather != "rainy": # conditons True or False
    print("the weather is not rainy. enjoy it as much as you can")
else:
    print("thank you for your time")`

# Let's use our ticket age criteria

`age = 18
if age <= 18: # checking the condition according to the age given
    print("you are not eligible to this movie, please select an under 18 rated movie")`

### For loops and while loops
### Loops helps us iterate through our data, such as lists, dicts, sets etc

`shopping_list = ["eggs", "apples", "milk", "bread", "butter", 1, 2 , 3 , 4]
                #   0       1         2       3         4
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])`
# Let's see we can get it done with for loop by iterating through our list
# first iteration:
# for items in shopping_list:
#     print(items)

# Second iteration with if conditions and control the flow of our program
`shopping_list = ["eggs", "apples", "milk", "bread", "butter", 1, 2 , 3 , 4]
for items in shopping_list:
    if items == "bread": #if condition is met
        break # stops the loop as soon as it meets the requirements
    print(items)`
    
# Third iteration with dict
`student_data = {
    "student_name": "Dini",
    "course": "Devops",
    "course_topics": 4,
    "topic_names" : ["Business week", "Python", "Virtualization with", "AWS cloud"]}#list
print(student_data)`

`for data in student_data.values:
     if data == "Dini": # if the condition is True the loop exit
        print(data)
    # In any case for loop would iterate through the data will be the last item`
#  While loops is essentially used to monitor the data
## First iteration of a while loop
`num = 0
while num < 10:
    print(f"Its working  -> {num}")
     num += 1 # adding 1 into num val each time it iterates through`
    
# Second iteration of a whole loop

`num = 0
while num < 10:
    print(f"it's working {num}")
    if num == 5: # as soon as this condition is true it would exit
        break
    num += 1`
## let'see how we can interact with our user in the third iteration
### prompt the user to input age and restrict to enter in digits only
### check if the data is in digits display it back to the user if not in digits prompt the user with message to enter in digits

`user_prompt = True
while user_prompt:
    age = input(" What is your age? ")
    if age.isdigit():
        user_prompt = False
    else:
        print("Enter in digits ")`



