# 1:Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

user_in = (input("Please tell us your name and nickname.No more than 10 characters:"))
user_int = len(user_in)

# if user_int < 10:
#     print("String not long enough")
# else:
#     print("string too long")

# 2: Then, print the first and last characters of the given text.

# last_char = user_in[-1]
# first_char = user_in[0]
#
# print(first_char, last_char)

#3: Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
#
# for i in user_in:
#     print(i)
# 4. Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:
import random
l = list(user_in)
random.shuffle(l)
print(l)