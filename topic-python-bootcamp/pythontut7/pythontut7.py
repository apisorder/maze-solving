
# Programmer:     Cheng, Jeff
# Last Modified:  08-28-2024 05:57PM
# Problem:        Python Tutorial 7

rand_string1 = "     this is an important string         "
print("rand_string1 = ", rand_string1)
rand_string2 = "     this is an important string         "
print("rand_string2 = ", rand_string2)
rand_string3 = "     this is an important string         "
print("rand_string3 = ", rand_string3)

rand_string1 = rand_string1.lstrip()
print("rand_string1.lstrip() = ", rand_string1)
rand_string2 = rand_string2.rstrip()
print("rand_string2.rstrip() = ", rand_string2)
rand_string3= rand_string3.strip()
print("rand_string3.strip() = ", rand_string3)

print("rand_string1.capitalize() = ", rand_string1.capitalize())
print("rand_string1.upper() = ", rand_string1.upper())
print("rand_string1.lower() = ", rand_string1.lower())

#   turn list into a string
a_list = ["Bunch", "of", "random", "words"]
#   delimiter = something used to separate data
print(" ".join(a_list))

#   turn string into a list
a_list_2 = rand_string1.split()
print("a_list_2 = ", a_list_2)

#   how many times a string occurs in another string
print("How many is : " + str(rand_string1.count("is")))
print("Where is : ", rand_string1.find("string"))
print("Replacing specific parts of a string", rand_string1.replace(" an", "a kind of"))

#   create an acronym generator
strings = input("Enter a string for the acronym : ")
print("The string you entered = ", strings)
string_as_list = strings.split()
acronym = ""
for string in string_as_list:
    acronym += string[0].upper()
print("The resulting acroynm = ", acronym)

#   official solution
orig_string = input("Convert to Acronym : ")
orig_string = orig_string.upper()
#   if no argument is given, split separates the string by space
list_of_words = orig_string.split()
for word in list_of_words:
    print(word[0], end="")
print()

letter_z = "z"
print("Is z a letter or a number? ", letter_z.isalnum())
print("Is z a letter? ", letter_z.isalpha())
print("Is z a number? ", letter_z.isdigit())
print("Is z lower case? ", letter_z.islower())
print("Is z upper case? ", letter_z.isupper())
print("Is z whitespace? ", letter_z.isspace())

#   rack the brain
#   Caesar cipher

#   1.  Receive a message and then encrypt it by shifting the characters by a requested amount to the right
#   i.e. A becomes D, B becomes E for example.  Also, decrypt the message back again.

#   Hints:
#   1.  A-Z have the numbers 65-90 in unicode
#   2.  a-z have the numbers 97-122
#   3.  You get the unicode of a character with ord(yourLetter)
#   4.  You convert from unicode to character with chr(yourNumber)
#   5.  Use isUpper() to decide which unicodes to work with
#   6.  Add the key (number of characters to shift) and if bigger or smaller than the unicode for A, Z, a, or z,
#   increase or decrease by 26

secret_message = input("Enter a secret message to send : ")
secret_key = int(input("Enter the number of digits to shift right (i.e. 1-26) : "))

encrypted_message = ""

#   encrypt the message
for char in secret_message:
    #   if it's a letter
    if char.isalpha():
        #   independent of its case, all letters are processed similiarly

        secret_code = ord(char)
        secret_code += secret_key

        #   if it's capitalized
        if char.isupper():
            if secret_code > ord('Z'):
                secret_code -= 26
            elif secret_code < ord('A'):
                secret_code += 26
        #   otherwise it must be lower-cased
        elif char.islower():
            if secret_code > ord('z'):
                secret_code -= 26
            elif secret_code < ord('a'):
                secret_code += 26
        
        encrypted_message += chr(secret_code)
    #   if it's not a letter, just add it, as is
    else:
        encrypted_message += char

print("Encrypted message = ", encrypted_message)

#   reverse the key
secret_key = -secret_key

decrypted_message = ""

#   now decrypt the message
for char in encrypted_message:
    #   if it's a letter
    if char.isalpha():
        secret_code = ord(char)
        secret_code += secret_key

        #   case by case
        if char.isupper():
            #   remembe to compare like to like
            if secret_code > ord('Z'):
                secret_code -= 26
            elif secret_code < ord('A'):
                secret_code += 26

        elif char.islower():
            if secret_code > ord('z'):
                secret_code -= 26
            elif secret_code < ord('a'):
                secret_code += 26

        decrypted_message += chr(secret_code)
    else:
        decrypted_message += char
        
print("Message deciphered as : ", decrypted_message)