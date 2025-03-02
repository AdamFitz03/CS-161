# Adam Fitzpatrick
# Week 8
import time
import math

#1
phrase = input("Please enter a phrase: ")
upper_phrase = input("Please enter the same phrase in all uppercase: ")

if upper_phrase == phrase.upper(): # compares if both phrases are the same by converting the initial phrase to uppercase.
    print("Stop shouting please!\n")
else:
    print("Thanks\n")

#2
vowels = ["a","e","i","o","u"]

user_vowels = input("Please enter a word or phrase: ").lower() # by default incorrect entry types, contain zero vowels.
unique_vowels = set() # used a set instead of a list, because sets do not store duplicate characters

for char in user_vowels: # Checks each character in the user intput to see if it has any vowels
    if char in vowels:
        unique_vowels.add(char) # If a vowel is found it adds it to the set unique_vowels

if len(unique_vowels) == 0:
    print(f"{user_vowels} has no vowels.\n")
else:
    print(f"{user_vowels} has {len(unique_vowels)} vowels.\n")

#3
phrase_one = input("Please enter a phrase: ")
phrase_two = input("Please enter a second phrase: ")

checker = (phrase_one < phrase_two) # compares the two inputs to see if the firs phrase is in alphabetical order compared to the second and stores a true/false value.

if checker == True: # print statements based off the true false value.
    print(f"{phrase_one} comes before {phrase_two}\n")
else:
    print(f"{phrase_two} comes before {phrase_one}\n")

#4
attempts = 4
while attempts > 0:
    email_one = input("Enter your email address: ")
    email_two = input("Enter your email address again: ")
    if email_one == email_two: # checks to see if both emails are the same.
        print("Thank you! for verifying your email address\n")
        break
    else:
        attempts -= 1 # if not the same, an attempt comes off the board.
        if attempts > 0: # nested if statement to allow for a different output when attempts run out.
            print(f"Entries do not match. {attempts} attempts remaining.\n")
        else:
            print("\nToo many incorrect entries. Account has been destroyed.\n")


#5
# All functions below makes use of the built-in python counter to display the processing time in nanoseconds
# I found this fun to compare a lot of values, so I am including a simple Excel sheet with results.
# However, I have found that the built-in function is the quickest and recursion is the slowest in processing times.
# I have also found that results vary each time I ran the functions, I wonder if this is due to the timing of my CPU?

# recursive
def fact_recursion(x):
    """Starts with an input number and multiplies it by itself minus 1 and keeps calling upon itself until reaching zero """
    if x < 0:
        print("No Negative numbers!!! RAAAA\n")
        return 0
    elif x == 0:
        return 1
    else:
        return x * fact_recursion(x - 1)

user_int = int(input("Please enter a number: "))

start = time.perf_counter_ns() #Starts counting
print(f"The factorial of {user_int} is: {fact_recursion(user_int)}\n")
stop = time.perf_counter_ns() #stops counting

print(f"Process took {stop - start} nanoseconds.\n") # prints count

# iterative
def fact_iterative(num):
    """ Function using iteration to multiply all digits in the "range" of an input number. I.E "5" would be 5x4x3x2x1. Except, this starts at 2 and works upwards.
        The reason for starting at 2,is because multiplying by one changes nothing. """
    fact = 1 # starts at one
    if num < 0:
        print("No Negative numbers!!! RAAAA\n")
        return 0
    for i in range(2, num + 1): # Starts at the second value in the factorial number and keeps counting upwards
        fact *= i # multiples the number by each number leading up to the factorial number
    return fact

user_two = int(input("Please enter enter a number: "))

begin = time.perf_counter_ns()
print(f"The factorial of {user_two} is: {fact_iterative(user_two)}\n")
end = time.perf_counter_ns()

print(f"Process took {end - begin} nanoseconds.\n")

# built-in python function to calculate factorials for comparison.
user_three = int(input("Please enter enter a number: "))
go = time.perf_counter_ns()
print(f"The factorial of {user_three} is: {math.factorial(user_three)}\n")
not_go = time.perf_counter_ns()

print(f"Process took {not_go - go} nanoseconds.")
