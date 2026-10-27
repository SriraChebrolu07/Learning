#       1.Write a Python program to make combinations of 3 digits.
#       2.Write a Python program to find the median among three given numbers.
#       3.Write a Python program to get all possible two-digit letter combinations from a 1-9 digit string.

#       string_maps = {
#       "1": "abc",
#       "2": "def",
#       "3": "ghi",
#       "4": "jkl",
#       "5": "mno",
#       "6": "pqrs",
#       "7": "tuv",
#       "8": "wxy",
#       "9": "z"
#       }
#       4.How to connect sql database and getting data with any table using python?





########################################################

#11111111111111111111



# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             # Print the combination of 3 digits
#             print(f"{i}{j}{k}")


#2222222222222222222
            
# list= [2,5,0]
# list.sort()
# print(list.length())
# print(list[1])


# import math
# list=[5,4,36,7,1,2,13,0,9]
# list.sort()
# print(list)
# i= len(list)/2
# a= math.ceil(i) 
# print(list[a])




#4444444444444444444444444444

string_maps = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tuv",
    "8": "wxy",
    "9": "z"
}

number = input("Enter two digits ")

digit1char = string_maps.get(number[0], "")
digit2char = string_maps.get(number[1], "")
combinations = []

for char1 in digit1char:
        for char2 in digit2char:
            combinations.append(char1 + char2)
    
print(combinations)


# if len(number) != 2:
#     print("Please provide exactly two digits")
# else: