
# Programmer:     Cheng, Jeff
# Last Modified:  05-31-2024 08:48AM
# Problem:        Python Tutorial 2

import math

name = input("What is your name : ")
print("Hello", name)
num_1, num_2 = input("Enter two numbers : ").split()
num_1 = int(num_1)
num_2 = int(num_2)
print("num_1 = ", num_1, ", and name_2 = ", num_2)
print("{} + {} = {} ".format(num_1, num_2, num_1 + num_2))

#   Challenge
#   Ask the user to input the number of miles

#   You'll convert miles to kilometers (kilometers = miles * 1.60934)

#   Then print this for example 5 miles equals 8.0467 kilometers

numOfMiles = float(input("Enter the number of miles to convert : "))
print("Number of miles entered = ", numOfMiles)
numOfKilometers = numOfMiles * 1.60934
print("Number of kilometers converted = ", numOfKilometers)

print("math.ceil(4.4) = ", math.ceil(4.4))
print("math.floor(4.4) = ", math.floor(4.4))
print("math.fabs(-4.4) = ", math.fabs(-4.4))
print("math.factorial(4) = ", math.factorial(4))
print("math.fmod(5,4) = ", math.fmod(5, 4))
print("math.trunc(4.2) = ", math.trunc(4.2))
print("math.pow(2, 2) = ", math.pow(2, 2))
print("math.sqrt(4) = ", math.sqrt(4))
print("math.e = ", math.e)
print("math.pi = ", math.pi)
