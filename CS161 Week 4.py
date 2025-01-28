# Adam Fitzpatrick
# Week 4 Python assignment
# !READ ME! This assignment is not account for input errors, wrong input values will result in having to restart.
#1
def average (a,b,c):
    ''' defines a function "Average" which takes the average value of three numbers
        by adding them together and dividing the sum by 3 '''
    return (a+b+c)/3
print(average(4,17,3))
print(average(90,2,14))
print()
#2
#print(average2(90,2,14))
#print(average2(90,2,14))

def average2 (x,y,z):
    ''' No this will not work as the print statement is trying to call
    a function that hasn't been defined yet. '''
    return (x+y+z)/3

#3
def average3(one,two,three):
    ''' This one, two, and three are inputs for the function they have not been assigned
        any values or been defined, so you cannot print out the input as is. '''
    return (one+two+three)/3

print(average3(4,17,3))
print(average3(90,2,14))
#print(one) This will not work as "one" is the placeholder for an input and hasn't been defined or assigned a value
print()
#4
def my_dog(woof):
    ''' defines a function to calculate dog year equivalency to human years.
        It starts by taking the input value "woof" and running it through the
        dog_to_human, math machine then prints the result using an f string
        you can change or test different values by changing the number in my_dog() below '''
    dog_to_human = 24 + (woof - 2) * 4
    print(f"{woof} dog years is the same as {dog_to_human} human years.")

my_dog(5)
my_dog(11)
print()
#5
def price_O_matic (price,age,make):
    ''' This function calculates a cars value after __ years of ownership. Using a flat percent amount taken off each year.
        This does not calculate the depreciation rate as that would require the value taken off each year to change based off the
        previous years value.

        The function takes an input of "make" and matches it to a list corresponding list for which country it is from.
        It then uses the country to determine the rate for which value is lost. If the make is not found it returns an error.
        Finally, the function calculates the cars value based off of the price of the car minus the (loss per year x number of years of ownership.),
        With loss per year being calculated as price - (price x the rate)
        and returns the calculated value in an f string.'''

    german = ["mercedes", "audi", "bmw", "porsche", "volkswagen"]
    japan = ["honda", "toyota", "subaru", "nissan", "mazda", "lexus", "mitsubishi", "hyundai"]
    italy = ["ferrari", "fiat", "lamborghini", "maserati"]
    us = ["chevrolet", "dodge", "telsa", "gmc", "buick", "ford", "cadillac", "jeep", "lincoln", "oldsmobile" ]
    if make in german:
        rate = 0.95
    elif make in japan:
        rate = 0.93
    elif make in italy:
        rate = 1.05
    elif make in us:
        rate = .90
    else:
        print("Sorry make not in list please check spelling./n If spelling is correct, make isn't found.")
        return
    loss_year = price - (price * rate)
    new_value = price - (loss_year * age)
    print(f"Your {make}, is worth ${new_value:0,.2f} after {age} years of ownership.")

car_price = float(input("Without using a comma (ex. 56,000 = 56000) How much was you car: $"))
car_age = float(input("How many years have you had your car?: "))
car_make = input("What make is you car?: ").lower()

price_O_matic(car_price,car_age,car_make)
print()
#6
def best_friend (bark):
    """ Simple function returning the user input of their dogs age and converting
        it to human year equivalent, uses a return statement to do the math
        and f string to print the results. Does NOT account for input type errors."""
    return 24 + (bark - 2) * 4

print("!Dog to Human Age Converter!")

dog_name = input("What is your dogs name?: ")
dog_age = int(input("What is your dog age?: "))

print(f"{dog_name} is {best_friend(dog_age)} years old in human years.")
print()
#7
def ice_cream (yummy):
    """ Simple function nearly identical to the one above (best_friend)
        except the return statement uses a different equation for the results."""
    return (yummy * 1.15) + 2.25

print("!How expensive is your ice cream?!")

num_scoops = int(input("How many scoops of ice cream do you want?: "))
print(f"{num_scoops} scoops of ice cream will cost you ${ice_cream(num_scoops):0,.2f}")
print()
#extra credit

# The dictionary of ice cream prices, sorted by year and months in order
price_dictionary = {
    2014: [5.022, 4.979, 4.842, 5.011, 4.911, 4.691, 4.719, 4.751, 4.987, 4.884, 4.863, 5.041],
    2015: [5.089, 4.955, 4.889, 4.791, 4.696, 4.620, 4.466, 4.597, 4.791, 4.626, 4.684, 4.725],
    2016: [4.913, 4.851, 4.850, 4.915, 4.801, 4.710, 4.691, 4.710, 4.695, 4.712, 4.615, 4.682],
    2017: [4.834, 4.870, 4.751, 4.659, 4.631, 4.629, 4.606, 4.688, 4.648, 4.683, 4.567, 4.758],
    2018: [4.786, 4.670, 4.825, 4.709, 4.588, 4.656, 4.750, 4.662, 4.754, 4.864, 4.786, 4.812],
    2019: [4.912, 4.981, 4.791, 4.821, 4.850, 4.633, 4.674, 4.682, 4.802, 4.940, 4.935, 4.740],
    2020: [4.824, 4.884, 4.918, 4.941, 4.934, 5.088, 4.898, 4.950, 4.944, 4.925, 4.846, 4.927],
    2021: [5.014, 4.937, 4.949, 4.978, 4.685, 4.886, 4.943, 4.918, 4.900, 4.952, 4.770, 4.766],
    2022: [4.993, 5.048, 5.059, 5.129, 5.352, 5.536, 5.621, 5.638, 5.701, 5.745, 5.724, 5.561],
    2023: [5.809, 5.722, 5.920, 5.950, 5.807, 5.812, 5.845, 5.904, 5.959, 6.041, 6.014, 6.015],
    2024: [5.903, 5.885, 5.733, 6.196, 6.000, 6.137, 6.030, 6.357, 6.338, 6.295, 6.447, 6.270]
}
# A month dictionary, allowing a user to enter a month name, that then pairs it with an index number
month_dictionary = {"JAN":0, "FEB" :1, "MAR":2, "APR":3, "MAY":4, "JUN":5, "JUL":6, "AUG":7, "SEP":8, "OCT":9, "NOV":10, "DEC":11 }

def price_history(year, month):
    """ Function that takes the inputs for user_year and user_month and uses them to access a spot in the dictionaries above.
        It does this by first taking the user_month str and matching it to an int. Then the function takes that user year
        and the month now in int form to access an item indexed in the dictionary. Finally it prints the resulting ice cream
        price in an f string"""
    month_number = month_dictionary[month]
    price = price_dictionary[year][month_number]
    print(f"The price of Ice Cream in {user_month}, {user_year} was ${price:.2f}")

print("!Ice cream price finder!")
user_year = int(input("Please enter a four digit year between 2014-2024: "))
user_month = input ("Please enter a month using the 3 digit abbr. ex.'JAN': ").upper()
price_history(user_year, user_month)