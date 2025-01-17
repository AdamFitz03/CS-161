#Adam Fitzpatrick week 2 assignment

#1:
while True:
    try:
        input_value = int(input("Enter a value to see binary and hexadecimal equivalents: "))
        break
    except ValueError:
        print("Invalid Input, please only input integers.")

print(f"{input_value} has a binary value of: {bin(input_value)} and a hexadecimal value of: {hex(input_value)} \n")

#2:
value = 18
print(value, bin(value), hex(value), "\n")
#1.825 return the's error TypeError: 'float' object cannot be interpreted as an integer
#Decimal numbers would have to be represented as a number to the negative number, if I understand correctly

#3:
binary_value = 0b11010
hex_value = 0x58
print(binary_value, hex_value, "\n")


#4:
variables_sum = value + binary_value  + hex_value
print('The sum of values from part 2 and 3 are' ,variables_sum, "\n")


#Compression:

document_size = 240
dictionary_size = 25
compressed_size = 148

percent_compressed = 1 - ((compressed_size + dictionary_size) / document_size)

print(f"Compressed text size: {compressed_size} characters \nDictionary size: {dictionary_size} characters \nTotal size: {compressed_size + dictionary_size} characters")
print(f"Original text size: {document_size} characters \nCompression: {percent_compressed:.2%}\n")

#extra credit:
# This took me a while, I understood how two's complements are found, but writing it in code took some trial and error as I got hung up on using the ~ bitwise function.

while True:
    def twos_complement (d):
        """ The function, takes a users input decimal and determines whether it's positive or negative. If it positive it prints
            the binary value formatted to 8 spots with the '0b' removed.

            If the value is negative, it takes the absolute value of that number and in a formated binary form and then
            flips all the values by replacing 0's with 1's. Then it joins it into a base 10 binary string and adds 1 to it.
            finally it prints the value."""

        if d >= 0:
            print(bin(d)[2:].zfill(8))
        else:
            abs_bin = (bin(abs(d))[2:].zfill(8))
            ones_bin = ''.join('1' if bit == '0' else '0' for bit in abs_bin )
            twos_bin = bin(int(ones_bin, 2) + 1)[2:].zfill(8)
            print(twos_bin)
    while True:
        try:
            user = int(input("Enter a positive or negative number: "))
            twos_complement(user)
            break
        except ValueError:
            print("Please only enter a decimal value, please try again.")
    answer = input("Would you like to stop?: ").upper()
    if answer == "Y" or answer == "YES":
        quit()
    else:
        continue