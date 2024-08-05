
# Programmer:     Cheng, Jeff
# Last Modified:  06-17-2024 09:18PM
# Problem:        Python Tutorial 4

print("for i in [2, 4, 6, 8, 10]:")
for i in [2, 4, 6, 8, 10]:
    print("i = ", i)

#   starts at 0 unless specified
#   11 is excluded
print("for i in range(2, 11):")
for i in range(2, 11):
    print("i = ", i)    

#   how to test whether a number is even or odd
#   if you divide an even number by 2, it will not have any reminder
#   the modulous provides the remainder of a division

i = 6
print("Is 6 even : ", ((i%2)==0))

print("All the odd numbers from 1 to 20 : ")
for i in range(21):
    if (i%2) != 0:
        print(i)

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

# investment = float(input("investment amount : "))
# interest_rate = float(input("interest_rate : "))*0.01
# years_to_invest = int(input("how many years : "))

# end_amount = investment
# for i in range(years_to_invest):
# 	end_amount = end_amount * (1+interest_rate) 
# 	print("end amount at the end of year " + str(i) + " = " + str(end_amount))
