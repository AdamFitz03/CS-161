#Adam Fitzpatrick
#Week5 Python
#import pip
#pip.main(['install','requests']) install prompt if needed
#pip.main(['install','psutil']) install prompt if needed
import requests
import psutil

#1
# does not account for incorrect entry type. You could put a "while" statement to fix that.

user_num = int(input( "Please entire a number to see if it is divisible by 5: "))
divisor = 5 #You can change the divisor here if wanted.
if user_num % divisor == 0: # Sees if there is a remainder based on the divisor. If there isn't it prints yes, else it prints no.
    print(f"Yes! {user_num} is divisible by {divisor}.\n")
else:
    print(f"No. {user_num} is not divisible by {divisor}.\n")


#2.1
# Takes a user input converts it to all lower case and checks it against if/else statements to see if there is a match.
# Only accounts for 6 states/capitols, returns not found if it is the wrong input type or the state isn't in the list

user_state_1 = input("Please enter the state you'd like to know the capitol of: ").lower()

if user_state_1 == "hawaii":
    print(f"{user_state_1.title()} has the capitol of Honolulu.\n")

elif user_state_1 == "wyoming":
    print(f"{user_state_1.title()} has the capitol of Cheyenne.\n")

elif user_state_1 == "alaska":
    print(f"{user_state_1.title()} has the capitol of Juneau.\n")

elif user_state_1 == "colorado":
    print(f"{user_state_1.title()} has the capitol of Denver.\n")

elif user_state_1 == "indiana":
    print(f"{user_state_1.title()} has the capitol of Indianapolis.\n")

elif user_state_1 == "maine":
    print(f"{user_state_1.title()} has the capitol of Augusta.\n")

else:
    print(f"{user_state_1.title()} is not in the database.\n")



#2.2
# Giant dictionary of all states and capitols that I totally typed out my self.
states_capitols = {
    "alabama": "Montgomery",
    "alaska": "Juneau",
    "arizona": "Phoenix",
    "arkansas": "Little Rock",
    "california": "Sacramento",
    "colorado": "Denver",
    "connecticut": "Hartford",
    "delaware": "Dover",
    "florida": "Tallahassee",
    "georgia": "Atlanta",
    "hawaii": "Honolulu",
    "idaho": "Boise",
    "illinois": "Springfield",
    "indiana": "Indianapolis",
    "iowa": "Des Moines",
    "kansas": "Topeka",
    "kentucky": "Frankfort",
    "louisiana": "Baton Rouge",
    "maine": "Augusta",
    "maryland": "Annapolis",
    "massachusetts": "Boston",
    "michigan": "Lansing",
    "minnesota": "St. Paul",
    "mississippi": "Jackson",
    "missouri": "Jefferson City",
    "montana": "Helena",
    "nebraska": "Lincoln",
    "nevada": "Carson City",
    "new hampshire": "Concord",
    "new jersey": "Trenton",
    "new mexico": "Santa Fe",
    "new york": "Albany",
    "north carolina": "Raleigh",
    "north dakota": "Bismarck",
    "ohio": "Columbus",
    "oklahoma": "Oklahoma City",
    "oregon": "Salem",
    "pennsylvania": "Harrisburg",
    "rhode island": "Providence",
    "south carolina": "Columbia",
    "south dakota": "Pierre",
    "tennessee": "Nashville",
    "texas": "Austin",
    "utah": "Salt Lake City",
    "vermont": "Montpelier",
    "virginia": "Richmond",
    "washington": "Olympia",
    "west virginia": "Charleston",
    "wisconsin": "Madison",
    "wyoming": "Cheyenne"
}
user_state_2 = input("Please enter a state you'd like to know the capitol of: ").lower()

# If the input state is in the dictionary, then this "if statement" gets the capitol name and prints it out
if user_state_2 in states_capitols:
        capitol = states_capitols.get(user_state_2)
        print (f"{capitol} is the capitol of {user_state_2.title()}.\n")
else: # Typos, wrong input types and incorrect places, get an incorrect entry print statement.
    print(f"{user_state_2.title()} is not a valid entry.\n")

#2.3
user_state_3 = input("Please enter the state you'd like to know the capitol of: ")

match user_state_3: # Matches the user input to the state name using case. Then prints the capitol name.
    case "hawaii":
        print(f"{user_state_3.title()} has the capitol of Honolulu.\n")
    case "wyoming":
        print(f"{user_state_3.title()} has the capitol of Cheyenne.\n")
    case "alaska":
        print(f"{user_state_3.title()} has the capitol of Juneau.\n")
    case "colorado":
        print(f"{user_state_3.title()} has the capitol of Denver.\n")
    case "indiana":
        print(f"{user_state_3.title()} has the capitol of Indianapolis.\n")
    case "maine":
        print(f"{user_state_3.title()} has the capitol of Augusta.\n")
    case other:
        print(f"{user_state_3.title()} is not in the database.\n")

#3
def public_pool(age):
    ''' Simple function to find the test the input age of the user and returns a
        corresponding price to "enter the pool" using if/else statements.
        The function is called in a print statement that also uses the converted "int user input"
        as the functions input.

        The print statement is only used to confirm correct price matching and does nopt include dollar signs. '''
    if age < 2:
        return 0
    elif age < 12:
        return 3
    elif age < 61:
        return 6
    else:
        return 4
print(public_pool(int(input("How old are you?: "))))

#4
# uses requests to get all the text of "coccbobcat.com" and count how many times "160 appears"
# Typically returns zero, because the website uses a human validation request.
web_site = requests.get('https://coccbobcat.com')
web_site = web_site.text
txt_counter = web_site.count("160")
print(f'The substring "160" appears {txt_counter} times in the source code of https://coccbobcat.com.\n')

#5
#uses psutil.pids to find all the processes running on the pc and len to print the number instead of a process list.
num_processes = len(psutil.pids())
print(f"There are {num_processes} processes running on this pc.")