# Dictionary tasks:
# 1. Write a Python program to convert more than one list to a nested dictionary.
# 2.Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
# 3.Write a Python program to convert string values of a given dictionary into integer/float datatypes.
# 4.Write a Python program to filter even numbers from a dictionary of values.

# sql task:
# 1. Identify usuers who have made purchases totaling more than 10000 in the last month from the pu
# sql task:
# 1. Identify usuers who have made purchases totaling more than 10000 in the last month from the purchase table.
# the puchase table contains information about purchases including the usersid, date of purchase , productid,and amount spent.

#11111111111111111111111111111111

keys = ["a", "b", "c", "a", "b", "c"]
values = [1, 2, 3, 4, 5, 6]


Ndictionary = {}

for key, value in zip(keys, values):
    current_level = Ndictionary
    # Split the key into levels
    levels = key.split('.')
    
    for level in levels[:-1]:
        if level not in current_level:
            current_level[level] = {}
        current_level = current_level[level]
    current_level[levels[-1]] = value

print(Ndictionary)


# a={'name':{'roll:1'}, 'religion':{'caste':'ac'}}
# print(a)

# print(a.items())

# print(a['name'].keys())


#22222222222222222222222222222222222

# pairs = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

# dictionary= {}
# for key, value in pairs:
#     if key in dictionary:
#         dictionary[key].append(value)
#     else:
#         dictionary[key] = [value]

# print(dictionary)



#3333333333333333333333333333333

# dictionary = {"a": "1","b": "bye","c": "hi","d": "69","e": "8.25"}


# #converted = {key: (int(value) if value.isdigit() else float(value) if value.replace('.', '', 1).isdigit() else value) for key, value in dictionary.items()}
# converted = {}
# for key, value in dictionary.items():
#     try:
#         converted[key] = int(value)
#     except ValueError:
#         converted[key] = value

# #print(dictionary)

# print(converted)



#44444444444444444444444444444444

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
even = {key: value for key, value in dictionary.items() if value % 2 == 0}



print(even)

