# Week 3 homework
# Adam Fitzpatrick

#1
# asks for and prints the user's name
user_name = input("Please, enter your name: ")
print("Hello " + user_name)

#2
#asks for and prints user's age plus 5 years
#gives an error message because user input needs to be converted to am integer, python doesn't want to math words.
#user_age = input("Please, enter your age: ")

user_age = int(input("Please, enter your age: "))
print("In 5 years you will be " + str(user_age + 5))

#3
#decided to make a loop on this one to verify that the user is only entering integer values.
#if they don't it prints an error message and has them try again.
while True:
    try:
        #asks the user for a number to add to their age.
        user_insight = int(input("How many years would you like to add to your age?: "))
        break
    except ValueError:
        print("Please only enter an integer, try again.")

#Uses the users entered age from number 2 and adds the amount of years they requested to it.
user_older = user_age + user_insight

#prints a concatenated message with the beginning and finishing ages converted to strings.
print("In " + str(user_insight) + " years you will be " + str(user_older) + " years old.")

#4
#asks user for their wage and hours worked and allows decimals using float(input
user_hours = float(input("How many hours did you work this week?: "))
user_wage = float(input("What is your hourly wage? (don't include the $): "))

#5
#long print string using concatenation to find results of weekly and yearly pay based off user_hours, and wage. Formated.
print("Your weekly pay before taxes is: $" + "{:,.2f}".format(user_wage * user_hours) + "\n" + "Your estimated annual pay is: $" + "{:,.2f}".format((user_wage * user_hours) * 52))

#6 extra credit

user_gross = (user_wage * 40) * 50 # takes the input for user_wage above and calculates an annual pay, based off 40 hours a week and 50 weeks a year.

# series of simple, if/else statements to find the remaining amount after taxes are taken out based off of income brackets.
# This is done by multiplying the gross income by the percentage of taxes that was NOT taken out.
if user_gross <= 11600.00:
    user_net = (user_gross * .9)

elif user_gross <= 47150.00:
    user_net = (user_gross * .88)

elif user_gross <= 100525.00:
    user_net = (user_gross * .78)

elif user_gross <= 191950.00:
    user_net = (user_gross *.76)

elif user_gross <= 243725.00:
    user_net = (user_gross *.68)

elif user_gross <= 609350.00:
    user_net = (user_gross * .65)

else:
    user_net = (user_gross * .88)

# printing the formated amounts
print("Based off your hourly rate, if you worked 40 hours a week and 50 weeks a year.")
print("Your annual gross pay would be: $" + '{:,.2f}'.format(user_gross))
print("Your annual net pay after taxes would be: $" + '{:,.2f}'.format(user_net))






