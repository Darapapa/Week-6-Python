# Exercise 1 : Convert Lists Into Dictionaries.Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# dict_from_list = dict(zip(keys, values))
# print(dict_from_list)

# Exercise 2 : Cinemax 2.Instructions
# “Continuation of Exercise Cinemax from Week4Day2 XP”
#
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# How much does each family member have to pay ?
# Print out the family’s total cost for the movies.
# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# ages = family.values()
# total_price = []
#
# for i in ages:
#     print(i)
#     if i < 3:
#         print('you buyed the baby ticket')
#     elif i in range(3, 13):
#         print('your ticket price is 10 $ ')
#         total_price.append(10)
#     else:
#         print('your ticket price is 15 $ ')
#         total_price.append(15)
# print(type(total_price))
# print('the total price is  ', sum(total_price))

# Exercise 3: Zara. Instructions
# Here is some information about a brand.
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# brand = {
#     'name': 'Zara',
#     'creation_date': 1975,
#     'creator_name': 'Amancio Ortega Gaona',
#     'type_of_clothes':['women', 'children', 'home'],
#     'international_competitors': ['gap', 'h&m', 'Benetton'],
#     'number_stores' : 7000,
#     'major_color':{
#         "France": 'blue',
#         'Spain' :'Red',
#         'US':['pink', 'green'],
#         'creation_date': 1975,
#         'number_stores': 10.000,
#     },
# }

# 3. Change the number of stores to 2.
# brand.update({'number_stores': 2})

# 4. Print a sentence that explains who Zaras clients are.
# print('Zara clients are who loves our brand ', brand['name'])

# 5. Add a key called country_creation with a value of Spain.
# brand.update({'country_creation': 'Spanish'})

# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# for i in brand:
#     if i == 'international_competitors':
#         brand.update({'international_competitors': ('gap', 'h&m', 'Benetton')})
#         print(brand)

# 7. Delete the information about the date of creation.
# del brand["creation_date"]

# 8. Print the last international competitor.
# print(brand['international_competitors'][-1])

# 9. Print the major clothes colors in the US.
# print(brand['major_color']['US'])

# 10. Print the amount of key value pairs (ie. length of the dictionary).
# print(len(brand))

# 11. Print the keys of the dictionary.
# print(brand.keys())

# 12. Create another dictionary called more_on_zara with the following details:
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ? cant have space or any other letter in the number key
# more_on_zara = {
#     'creation_date': 1975,
#     'number_stores': 10000,
# }
# print(more_on_zara)
#
# brand.update(more_on_zara)
# print(brand)


# Exercise 4 : Disney Characters
# Instructions.Use this list :Analyse these results :
# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]

#1/ {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# my_dict = dict()
# for key, index in enumerate(users):
#     my_dict[index] = key
# print(my_dict)



# my_dict = dict()
# for key, index in enumerate(users, 1):
#     my_dict[index] = key
# print(my_dict)

#2/ {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#3/
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.














