# Adam Fitzpatrick
# Week 6 Assignment

#1
user_value = int(input("Please pick a number: ")) #only accounts for integer inputs, no strings or floats allowed.

while user_value > 0: # Has to be a positive int value
    print(user_value)
    user_value -= 1 # Counts down
print("BOOM!\n") # Boom

#2
value_two = int(input ("Please pick a number: "))

while value_two > 0: # same loop as #1 but needed to put the count on both even and odd to print starting value
    if value_two % 2 == 0: # determines if a number is even, byt dividing by 2 and seeing if there is a remainder.
        print(f"{value_two} is even")
        value_two -= 1
    else:
        print(f"{value_two} is odd")
        value_two -= 1
print("BOOM!\n")

#3
user_num = int(input("Please pick a number: "))
user_decrease = int(input("Please pick a number to decrease your number by: "))

while user_num > 0: # Same as the two loops above, but it is using the value entered in user_decrease instead of 1 as the increment.
    if user_num % 2 == 0:
        print(f"{user_num} is even")
        user_num -= user_decrease
    else:
        print(f"{user_num} is odd")
        user_num -= user_decrease
print()
#4.1
testing = 3 #allows the loop to end, can also type a word under five letters.
while testing > 0 : # uses a while loop to test if the condition is true (word being 5 letters or more) if it's not it breaks the loop.
    user_word = input("Please pick a word: ")
    if len(user_word) >= 5:
        print(f"{user_word} has {len(user_word)} letters\n")
        testing -= 1
    else:
        print("Addios!\n")
        break

#4.2
test_2 = 3 #allows the loop to end, can also type a word under five letters or over five letters.
while True: # Same loop as 4.1 but added a condition to break the loop if the word is greater than 5 letters.
    word_two = input("Please pick another word: ")
    if len(word_two) == 5:
        print(f"{word_two} has {len(word_two)} letters\n")
        test_2 -= 1
    elif len(word_two) > 5:
        print("Nerd!\n")
        break
    else:
        print("Addios!\n")
        break

#5
value = 10
while value >= 10 and value <= 100: # while loop that counts upwards to 100 as long as the value is in range. Else it quits.
    print(value, bin(value), hex(value)) # print int, binary, and hex values for "value"
    value += 1
print()

#6.1
def iterative(x):
    '''iterative function that uses a while loop to count down from the input value, but replaces the numbers with astrix.1
    '''
    while x > 0:
        for i in range(x):
            print("*",end="") #formats the astrix horizontally
        print() #formats so that each new number prints on the next row.
        x -= 1
iterative(int(input("Please pick a number: ")))

#6.2
def recursion(y):
    """recursion function that calls upon itself to keep subtracting 1 from the previous value until 0 is reached."""
    if y <= 0:
        print()
    else:
        print("*" * y)
        recursion(y - 1)

recursion(int(input("Please enter a number: ")))

#sum of digits
def sum_of_digits(number):
    ''' Recursive function that repeatedly divides the number by 10 and calls itself on the quotient,
        then adds the remainders together to produce the sum. If the number is less than zero it returns the number.'''
    if number < 10:
        return number
    else:
        return sum_of_digits(number//10) + number % 10
number_input = 99999999999999999999
print(f"The sum of all the digits in {number_input} is: {sum_of_digits(number_input)}")
print()


#Palidrome
words_left = 3 #The amount of times the function will repeat.
while words_left > 0: # Put the entire function in a while loop so you can test more than one word.
    def palindrome (word):
        ''' This function works by first checking if the word less than 2 letters,
            because by default a single letter word is in fact a palindrome.

             If the word is 2 letters and over the function checks to see if the first and last
             letters are the same, if they are the function recursively calls upon itself to verify matching letters
             by working inwards.'''

        word = word.lower()
        if len(word) < 2:
            return True
        elif word[0] == word[-1]: # verifies first and last letters are the same.
            return palindrome(word[1:-1]) # works inwards on the string
        else:
            return False

    words_left -= 1  # counts down the entire loop, so you're not stuck guessing palindrome words for all eternity.

    user_str = input("Please enter a word, to check if it is a palindrome: ")
    result = palindrome(user_str)
    
    if result == True: # If/else statement to allow for a better output than just True/False.
        print(f"{user_str} is a palindrome. You have {words_left} words left.\n")
    else:
        print(f"{user_str} is not a palindrome. You have {words_left} words left. \n")

