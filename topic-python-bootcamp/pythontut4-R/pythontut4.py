
# Programmer:     Cheng, Jeff
# Last Modified:  06-17-2024 09:18PM
# Problem:        Python Tutorial 4

your_float = input("Enter a float : ")
your_float = float(your_float)
print("Rounded to  2 decimals using:.2f {:.2f}".format(your_float))

#   your program will :
#   1. Have the user enter their investment amount
#   and their expected interest
#   2. Each year their investment will increase by their investment + their investment * the interest rate
#   3. Print out their earnings after a 10 year period

initial_investment_amount = float(input("How much to invest : "))
#   * 0.01 or / 100
the_interest_rate = float(input("Interest rate (enter numbers, such as 10 for 10%, or 10.5 for 10.5%): ")) * 0.01
cumulated_amount = initial_investment_amount
for year in range(1, 11):
    cumulated_amount = cumulated_amount + cumulated_amount*the_interest_rate
    print(cumulated_amount)
print("In 10 years, you will have " + str(cumulated_amount))

#   If you place an r before the beginning quotation mark of a string to make it a raw string,
#   it completely ignores all escape characters and prints any backslash that appears in the string.

print()
print("Printing a raw string....")
print(r"That is Carol\s cat.")

#   Because this is a raw string, Python considers the backslash as part of the string, and not as the start
#   of an escape character.  Raw strings are helpful if you are typing string values that contain many
#   backslashes, such as strings used for Windows file paths like r'C:\Users\Benny\Desktop' or regular
#   expressions.

#   While you can use the \n escape character to put a newline into a string, it is often easier to use
#   multiline strings.  A multiline string in Python begins and ends with either three single quotes or three
#   double quotes.  Any quotes, tabs, or newlines in between the "triple quotes" are considered part of the
#   string.  Furthermore, Python's indentation rules for blocks do not apply to lines inside a multiline
#   string.

print('''Dear Pat,
Katrina's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Al''')

#   Notice that the single quote characters in Katrina's does not need to escaped.  Escaping single and double
#   quotes is optional in multiline strings.  The following print() call would print identical text but doesn't
#   use a multiline string.
print('Dear Pat,\n\nKatrina\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nAl')

