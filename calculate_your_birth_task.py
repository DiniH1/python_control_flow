# Task 1
age = 22
name = "Dini"
DOB = 2021 - age
print(f"OMG {name}, you are {age}, so you must have been born in {DOB}")

# Task 2
user_prompt = True
name = input("What is your name? ")

while user_prompt:
    age = input("How old are you? ")
    if age.isdigit() == True and int(age) < 120:
        while user_prompt:
            birth_month = int(input("As a digit what month were you born in? "))
            if birth_month < 7 and birth_month > 0:
                DOB = 2021 - int(age)
                print(f"OMG {name.capitalize()} you are {age} so you were born in {DOB}")
                user_prompt = False
            elif birth_month > 6 and birth_month <= 12:
                DOB = 2020 - int(age)
                print(f"OMG {name.capitalize()}, you are {age} years old so you were born in {DOB}")
                user_prompt = False
            else:
                print("Invalid output! Ensure the month is written as a digit!")

hours_lived = int(age) * 8760
print(f"You have been alive for {hours_lived} hours!")


