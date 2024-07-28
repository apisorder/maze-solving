
# Programmer:     Cheng, Jeff
# Last Modified:  06-29-2024 07:38PM
# Problem:        Python Tutorial 5

#   random range module
import random

#   the end is not inclusive
rand_num = random.randrange(1, 51)

#   whenever you use a while loop, it's important that the value you want to increment 
#   inside the while loop is defined outside the while loop

i = 1
while i != rand_num:
    i += 1
print("The random value is ", i)

i = 1
while i <= 20:
    #   skipping even numbers
    if i%2 == 0:
        i += 1
        continue
    if i == 15:
        break
    print("Odd : ", i)
    #   remember to increment
    i += 1

#   the hardest problem so far
#   really push your brain to see if you can solve it

#   draw the pine tree

#   we count from height - 1 to 0
height = int(input( "How tall is the tree : " ))-1
#   how tall is the tree
#           #       -> 4 spaces
#          ###      -> 3
#         #####     -> 2
#        #######    -> 1
#       #########   -> 0
#           #       -> 4 spaces agin

#   Tip 1   use a while loop and 3 for loops
#   Tip 2   I know this is the number of spaces and hashes for the tree
#   4-1
#   3-3
#   2-5
#   1-7
#   0-9
#   spaces before stump = spaces before the top of your tree
#   Tip 3
#   You will need to do the following in your program : 
#   1.  Decrement spaces by one each time through the loop
#   2.  Increment the hashes by 2 each time through the loop
#   3.  Save spaces to the stump by calculating height - 1
#   4.  Decrement from tree height until it equals 0
#   5.  Print spaces and then hashes for each row
#   6.  Print stump spaces  and then 1 hash

bark = height-1
number_of_hashes = 1

pattern = ""
spaces = 0
hashes = 0
while height >= 0:
    while spaces <= (height-1):
        pattern += ' '
        spaces += 1
    while hashes < number_of_hashes:
        pattern += '#'
        hashes += 1
    print(pattern)
    pattern = ""
    spaces = 0
    hashes = 0
    number_of_hashes += 2
    height -= 1

number_of_hashes = 1
while spaces <= bark:
    pattern += ' '
    spaces += 1
while hashes < number_of_hashes:
    pattern += '#'
    hashes += 1
print(pattern)

#   official solution
tree_height = input("How tall is the tree : ")
tree_height = int(tree_height)
spaces = tree_height - 1
hashes = 1
stump_spaces = tree_height - 1

while tree_height != 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")
    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1

for i in range(stump_spaces):
    print(" ", end="")
print("#")