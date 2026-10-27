# 1.Write a Python program to create a flat list of all the keys in a flat dictionary.
# 2.Write a Python program to transform a dictionary into a list of tuples.
# 3.Write a Python program to find the maximum and minimum values in a set.
# 4.Write a Python program to check if a given set is a superset of itself and a superset of another given set.
# 5.Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.

#11111111111111111111111111

# dictionary = {"a": 1,"b": 2,"c": 3,"d":4,"e":5}

# keys = dictionary.keys()
# print(keys)
# listK=list(keys)
# print(listK)

#2222222222222222222222222222222

# dictionary={"a":1,"b":2,"c":3,"d":4,"e":5,"f":{"k":6}}
# y=dictionary.items()
# #print(y)
# mylist=list(y)
# print(mylist)

#333333333333333333333333

# set = {54, 14, 45, 79, 35, 0, 9, 19, -456, -1}

# max=0
# min=max

# # Find the maximum value
# for i in set:
#     if i > max:
#         max = i

# # Find the minimum value
# for x in set:
#     if x < min:
#         min= x
  
# print(min)
# print(max)


#4444444444444444444444444444444444444444444444

# set1 = {1,2,3,4,5,6,7,8,9,10}
# set2 = {1, 2, 3, 4, 5}

# if set1.issuperset(set2):
#     print("set1 is a superset of set2")
# else:
#     print("set1 is not a superset of set2")

# if set1.issuperset(set1):
#     print("yes, set1 is superset of itself")
# else:
#     print("not a superset of itself")



#555555555555555555555555555555555555555555
# strings = ["Python is a general-purpose programming language that is is"]

# words_count = {}
# unique_words = set()

# for string in strings:
#     words = string.split()

#     for word in words:
#         word = word.strip('.,!?')
#         if word:
#             unique_words.add(word)
#             words_count[word] = words_count.get(word, 0) + 1


# #  for word in unique_words: print(word)


# for word, frequency in words_count.items():
#     print(f"{word}: {frequency}")

string = ["Python is a general-purpose programming language that is is"]

words_count = {}

for i in string:
    print(i)
    for word in i.split():
        if word:
            words_count[word] = words_count.get(word, 0) + 1


for word, frequency in words_count.items():
    print(f"{word}: {frequency}")
