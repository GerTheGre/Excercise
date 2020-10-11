# this program will take name and age as an input and tell you what year will you turn 100 years old

import datetime

# when called will run until user inputs an integer. If any other datatype is input, user is asked to use whole number instead.
def get_age():
    while True:
        age_input = input("What is your age?: ")
        try:
            return int(age_input)
        except ValueError:
            print(f"Try a whole number instead.")

# checks your age and based on it will return a string with calculation what year have you turned hundred or will turn hundred years old
def hundred_in(age, name):
    if age < 0:
        return("In this universe you weren't born yet " + name + ". You will be 100 years old in the year " + str(cyear + 100 - age) + ".")
    if age < 100:
        return("Hello " + name + ". You will be 100 years old in the year " + str(cyear + 100 - age) + ".")
    if age == 100:
        return("Hello " + name + ". This year is your 100th birthday!.")
    if age > 100:
        return("Hello " + name + ". You turned 100 years old in the year " + str(cyear + 100 - age) + ".")

# getting current year
cyear = datetime.date.today().year
# getting users name
name = input("What is your name?: ")
# calling a fuction to get users age
age = get_age()

#final output
print(hundred_in(age, name))

