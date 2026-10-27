# 1.Write a program that takes a list of numbers and a set of numbers. For each number in the list, check if it exists in the set, and return a new set containing only those numbers that exist in both the list and the set.
# 2.Write a program that accepts a dictionary of people's names  and their ages, and returns a new dictionary containing the same data, but with the ages sorted in ascending order.(using lambda ,without using lambda).
# 3.Write a Python function that takes a string as input and returns a dictionary where keys are characters, and values are the frequencies of those characters in the string.
# 4.Nested List Comprehension:
# Create a 2D matrix (list of lists) using nested list comprehension.

#1111111111

# list = [5,6,4,9,14,2]
# sets = {5,14,65,87,3,99}
# result = set()

# for i in list:
#     if i in sets:
#         result.add(i)

# print(result)



#22222222 

# dictionary = {'ramarao': 25, 'sridhar': 39, 'rajesh': 24, 'rakesh': 33}
# dictionary2 = dict(sorted(dictionary.items(), key=lambda item: item[1]))
# print(dictionary)
# print(dictionary2)  #using lambda



# import operator
# dictionary = {'Alice': 25, 'Bob': 30, 'Charlie': 20, 'David': 35}
# dictionary2 = dict(sorted(dictionary.items(), key=operator.itemgetter(1)))
# print("Original dictionary:", dictionary)
# print("Sorted dictionary:", dictionary2)  #without lambda



#3333333333


# word = "celluloid"
# frequency= {}
# for i in word:
#     # Increment the frequency count for the current character
#     frequency[i] = frequency.get(i, 0) + 1
# print(frequency)


 

#44444444444

# matrix = [[1 for i in range(5)] for i in range(5)]

# print(matrix)




car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

