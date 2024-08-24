
# Programmer:     Cheng, Jeff
# Last Modified:  05-31-2024 03:13PM
# Problem:        Python Tutorial 3

#   Challenge
#   Enter Calculation: 5 * 6
try:

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
        
except ValueError:
    print("Unexpected error has occurred.")

#   condition_true if condition else condition_false
voter_age = int(input("What is your age ? "))
can_vote = True if voter_age >= 18 else False
print("You can vote : ", can_vote)