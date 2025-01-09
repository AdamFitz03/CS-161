#Adam Fitzpatrick Week 1 Assignment
#print()'s are for spacing between sections in the output.
import calendar
import datetime
print("My name is Adam and this is my week one assignment")

#part 1
pet_type = "Australian Shepards"
pet_names = ["Kaya","Kenzie"]

print()
print(f"I have two {pet_type} and their names are {pet_names[0]} and {pet_names[1]}!")
print()

#part 2
while True:
    try:
        name = input("What is your name? ")

        # Check that age is an integer
        age = int(input("What is your age? "))

        # Check that savings is an integer
        savings = int(input("What is your yearly savings? "))

        print()
        print(f"Hello {name}! You are {age} years old.")
        print(f"In 10 years you will be {age + 10} years old.")
        print(f"If you save ${savings} each year, in 5 years you will have ${savings * 5}.")
        print(f"Your average monthly savings is ${savings / 12:.2f}.")
        print()

        break # exits loop if inputs are correct

    except ValueError: # restarts questionnaire if answers are incorrect
        print("Only enter integers for age and yearly savings. Please try again")

#part 3
now = datetime.datetime.now()
current_month = calendar.monthrange(now.year, now.month)[1]
current_month_name = now.strftime("%B")
print(f"The current month is {current_month_name} and has {current_month} days or {current_month * 86400} seconds.")
print()

#part 4
num_eggs = int(input("How many eggs do you have? "))

print(f"You have {num_eggs // 12 } dozen eggs with {num_eggs % 12} left over.")
print()

print("goodbye!")