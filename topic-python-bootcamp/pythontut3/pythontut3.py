
# Programmer:     Cheng, Jeff
# Last Modified:  05-31-2024 03:13PM
# Problem:        Python Tutorial 3

drink = input("Pick One (Coke or Pepsi) : ")
if drink == "Coke":
    print("Here is your Coke")
elif drink == "Pepsi":
    print("Here is your Pepsi")
else:
    print("Here is your water")

#   Challenge
#   Enter Calculation: 5 * 6
leftOperand, operator, rightOperand = input("Enter an equation to calculate, separate by space (i.e. 5 * 7) : ").split()
if operator == "*":
    print(float(leftOperand)*float(rightOperand))
elif operator == "/":
    print(float(leftOperand)/float(rightOperand))
elif operator == "+":
    print(float(leftOperand)+float(rightOperand))
elif operator == "-":
    print(float(leftOperand)-float(rightOperand))
elif operator == "%":
    print(float(leftOperand)%float(rightOperand))

#   Age 1-18 -> Important
#   Age 21, 50, >65 -> Important
#   All others -> not Important

age = int(input("Enter age : "))

if age >= 1 and age <= 18:
    print("This is an important day (1-18): your birthday.")
elif age == 21 or age == 50:
    print("This is an important day (21 or 50): your birthday.")
elif age > 65:
    print("This is an important day (> 65): your birthday.")
else:
    print("Sorry, not an important birthday (NOT 1-18, 21, 50, or > 65).")

#   Age 5 -> "Go to Kindergarten"
#   Age 6 through 17 goes to Grade 1 through 12, "Go to Grade 6" 
#   If age is greater then 17 then say "Go to College"

student_age = int(input("Enter the age of the student : "))

if age <= 4:
    print("You are too young to attend school")
elif age == 5:
    print("Go to Kindergarten")
elif age >= 6 and age <= 17:
    print("Go to Grade " + str(age - 5))
else:
    print("Go to College")

#   condition_true if condition else condition_false
voter_age = int(input("What is your age ? "))
can_vote = True if voter_age >= 18 else False
print("You can vote : ", can_vote)