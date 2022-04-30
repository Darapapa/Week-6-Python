# Exercise 1 : Favorite Numbers.Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

# my_fav_number = {10, 18, 91, 11, 4}
# my_fav_number.update([5, 7])
# my_fav_number.discard(10)
# print(my_fav_number)

# friend_fav_number = {14, 42, 53, 63, 12}
# our_favorite_number = my_fav_number | friend_fav_number
# print(our_favorite_number)


# Exercise 2: Tuple.Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# NO!NO!NO!NO!NO!NO!NO!NO!NO!NO!NO!


# Exercise 3: Print A Range Of Numbers.Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.

# num = range(1, 21)
# for number in num:
#   print(number)


# Exercise 4: Floats.Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# 2 completely different datatypes.integer is a number without a decimal point while float have a decimal place

# Can you think of another way to generate a sequence of floats?
# import decimal
# def float_range(start, stop, step):
#   while start < stop:
#     yield float(start)
#     start += decimal.Decimal(step)
# print(list(float_range(0, 1, '0.1')))

# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# list = {1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5}

# Exercise 5: Shopping List
# Instructions
# Using this list
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
# basket.remove("Banana")
# Remove “Blueberries” from the list.
# basket.remove("Blueberries")
# Add “Kiwi” to the end of the list.
# basket.append("kiwi")
# Add “Apples” to the beginning of the list.
# basket.insert(0,"Apples")
# Count how many apples are in the basket.
# basket.count('Apples')
#  print(basket.count('Apples'))
# Empty the basket.
# basket.clear()
# print(basket)


# Exercise 6 : Loop.Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
# my_name = "Dani"
# user_input = input("Guess my name: ")
# while my_name != user_input:
#     user_input = input("wrong answe.Try again")

#
#
# Exercise 7 Instructions
# Given a list, use a loop to print out every element which has an even index.
# list = {"Dani" "Apa" "Anya" "Zoli" "paprika"}
# for j in list:
#     a = ""
#     b = ""
#     for i in range(0, len(j)):
#         if i%2 == 0:
#             a = a+j[i]
#         else :
#             b = b + j[i]
#     print(a)
#
# Exercise 8.Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

# number = 1500
# while number <= 2500:
#     number += 1
#     a = ()
#     b = ()
#     if number % 5 == 0 :
#         a = number
#     if number % 7 == 0:
#         b = number
#         print(a, b)

#
# Exercise 9: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).

# list_fav_fruit = input("Please tell me what is your favorite fruit.Please seperate your answer(s) with space: ")
# string_to_words = list_fav_fruit.split()
# any_fruit = input("Please type in any fruit: ")

# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
# for i in string_to_words:
#     if any_fruit in string_to_words:
#         print("Enjoy your favorite fruit")
#     if any_fruit not in string_to_words:
#         print("You chose a new fruit")


# Exercise 10: Who Ordered A Pizza ? Instructions
# Write a loop that asks a user to enter a series of pizza toppings,
# when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

# toppings = []
# order = ''
# price = 10
#
#
# while order != 'quit':
#     order = input("type in what toppings you want on your pizza or 'quit'")
#     if order != 'quit':
#         toppings.append(order)
#         print(order + " has been added to your order")
#     else:
#         toppings_price = 2.5 * len(toppings)
#         print("your toppings are", toppings, "and your bill is", toppings_price+price, )


# Exercise 11: Cinemax Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.

# baby_ticket_price = int(0)
# kid_ticket_price = int(10)
# adult_ticket_price = int(15)
# fam_mem_age = int()
# total_price = []
# pay = "pay"

# fam_mem_age = int(input('please enter the age of the person you want to buy the ticket for: '))
# for i in fam_mem_age:
#     if fam_mem_age < 3:
#         total_price.append(baby_ticket_price)
#         print('The free baby ticket has been added to your basket')
#     elif fam_mem_age <= 12:
#         total_price.append(kid_ticket_price)
#         print('One kid ticket price has been added to your basket')
#     if fam_mem_age > 12:
#         total_price.append(adult_ticket_price)
#         print('One adult ticket has been added to your basket')

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch the movie.


# names_list = ["Daniel", "Mikr", "Dada", "Kiraly"]
# for i in names_list :
#     age = int(input('What is your age? '))
#     if age in range(16, 22):
#         print('enjoy your movie')
#     elif age < 16:
#         names_list.remove(i)
#         print('you are not allowed to watch the movie sucker')

# Exercise 12 : Who Is Under 16?
# Instructions
# Given a list of names, write a program that asks every user for their age, if they are less than 16 years old remove them from the list.
# At the end, print the final list.

# names_list = ['Daniel', 'bobo', 'kirdul']
# for i in:
#     age = int(input('What is your age? '))
#
#     if age < 16 <= 21:
#         names_list.remove(i)
#     print(names_list)
# #
# Exercise 13
# Instructions
# Make a list called sandwich_orders and fill it with the names of various sandwiches .
# Then make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

# sandwich_orders = ["Tuna", "Bolo", "Druga", "Ok"]
# finished_sandwiches = []
#
# for szendvics in sandwich_orders:
#     finished_sandwiches.append(szendvics)
#     print('i made you a ' + szendvics + " Sandwich")

# Exercise 14
# Instructions
# Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

# sandwich_orders = ["Tuna", "Bolo", "Druga", "Ok", "Pastrami", "Pastrami", "Pastrami"]
# finished_sandwiches = []
#
# for szendvics in sandwich_orders:
#     print("Deli has run out of pastrami")
#     finished_sandwiches.append(szendvics)
#     while "Pastrami" in sandwich_orders:
#         sandwich_orders.remove("Pastrami")
#         finished_sandwiches.append(sandwich_orders)
#
#     print('i made you a ' + szendvics + " Sandwich")
