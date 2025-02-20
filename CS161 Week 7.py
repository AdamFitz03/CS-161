#Adam Fitzpatrick
#week 7

#1
user_min = int(input("Enter a min number: "))
user_max = int(input("Enter a max number: "))
number_list = ""
for n in range(user_min, user_max + 1): #loops through all numbers from user_min THROUGH user_max.
    if n % 2 == 0: # determines if the number is even.
        number_list += str(n) + " " # adds the numbers as a str to number_list.

print(f"All even numbers between {user_min} and {user_max} are: {number_list}")

#2
user_int = int(input("Enter a positive number: "))
x = 1
factors =[]
while user_int >= x: # determines the factors of a given number by seeing if the number divided by one has a remainder. the "one" is then incremented until it has the same value as the input number.
    if user_int % x == 0:
            factors.append(x) # adds all the numbers to a list.
    x += 1

print(f"All factors of {user_int} are: {factors}")


#3
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] # an alphabet list, copied and pasted from the homework instructions.
name = input("What is you last name?: ").lower() # input with case modifier
index_list = [] # empty list for storage
for letter in name:
# Loops through every char in the input and compares it to the alphabet list.
# If the char is found in the alphabet list then it store the index value of that character in "index_list"
    index_list.append(alphabet.index(letter))
print(f"The sum of all the letters in the name {name} is: {sum(index_list)}") # print statement that adds together all the digits of the new "index_list".

#4
def squares (n):
    """ Recursive function that calls that squares evey number up to the given number
        by calling upon itself one digit at a time until it reaches 0, at which point it prints,
         the result of the digit multiplied by itself."""
    if n > 0:
        squares(n - 1)
        print(n * n)

squares(int(input("Enter a number: ")))

#5
unsorted_list = [12, 43, 22, 34, 2, 21, 3, 33, 81] # starting list
evens = [] # empty list to store even numbers
odds = []  # empty list to store odd numbers
# loops through every digit in the list and determines if the digit is positive by seeing if it has a remainder when divided by 2.
# It then places the digits in the correct list and sorts the lists (the evens in reverse order).
# Finally, it joins the two lists starting with the odd list, to form a "Teepee" of values.
for i in unsorted_list:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
evens.sort(reverse=True)
odds.sort()
print(odds + evens)

#6
def next_permutation (array):
    """ This function is an algorithm called next permutation and looks for the next highest number available with the given digits.
        It has an O(n) time complexity and took me a lot of googling to figure out, but I learned a lot in the process.

        It does this by determining the pivot point, which is the smallest number to the left of the last number in the list.
        When it finds this number it stores it in the variable 'pivot'. If no smaller variable is found it returns none.

        Next the function looks for the smallest digit to the right of the pivot point that is larger than the pivot. Once found
        it stores the digit in the variable 'next_swap'.

        After the correct digits are located and stored, the function swaps those two digits and sorts everything to the right
        of the new 'pivot' location. The sort is in descending order.

        Finally, it prints the results. """

    n = len(array) # determines the length of the list, so we can identify the starting position.
    pivot = -1 # Sets the pivot variable to the last digit.

    for i in range(n - 2,-1,-1):# Reads through the entire list backwards, one step at a time, starting from the second to last position.
        if array[i] < array[i + 1]: # If the digit it's reading is less that the previous digit, it changes the pivot point to that digit.
            pivot = i
            break

    if pivot == -1: # if the last digit is the smallest it returns that no other arrangements can be made
        return None

    next_swap = -1 # "Holder" for the next smallest digit to swap starting at the end of the list.
    for i in range(n - 1, pivot, -1): # works the list backwards one step at a time, up to the pivot point, searching for the next smallest digit, lager than itself.
        if array[i] > array[pivot]: # if the digit is found it places it in the "next_swap" variable.
            next_swap = i
            break

    array[pivot], array[next_swap] = array[next_swap], array[pivot] # plays the swapping game with the pivot point, and the next smallest-largest digit.

    array[pivot + 1:] = reversed(array[pivot + 1:]) # sorts the list from the pivot point to end, in reverse order.
    return array


array = [9,5,2,1,7,6,0,8,3,4]
#array = [5,6,4,7,3,8,2,9,0,1] #alternate list.
result = next_permutation(array) # sets the function to a variable for print statements.

if result == None: # prints results with corresponding statements.
    print("No larger arrangement exists.")
else:
    print("Next larger arrangement:", result)

