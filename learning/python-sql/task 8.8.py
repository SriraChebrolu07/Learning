
# 1.set menthods and Dictionary methods.
# 2.Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type.
# 3.Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.
# 4.Write a Python program to find all the anagrams and group them together from a given list of strings. Use the Python data type.

# 5.Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.


#111111111111111111111111111
#dictionay menthods:

# data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# # keys()
# keys = data.keys()
# print( keys)

# # values()
# values = data.values()
# print( values)

# # items()
# items = data.items()
# print( items)

# # get()
# value = data.get('c')
# print( value)

# # update()
# dict2 = {'g': 7, 'h': 8}
# data.update(dict2)
# print(data)

# # pop()
# popped = data.pop('e')
# print(popped)
# print(data)

# # clear()
# data.clear()
# print( data)


# #set methods:


# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}


# set1.add(6)
# print( set1)


# set1.update([7, 8, 9])
# print( set1)


# set1.remove(9)
# print( set1)


# set1.discard(8)
# print(set1)

# popped = set1.pop()
# print( popped)
# print( set1)


# union = set1.union(set2)
# print(union)


# intersection = set1.intersection(set2)
# print( intersection)


# difference = set1.difference(set2)
# print( difference)


# symmetricDiff = set1.symmetric_difference(set2)
# print(symmetricDiff)


# disjoint = set1.isdisjoint(set2)
# print(disjoint)


# subset = {4, 5}
# is_subset = subset.issubset(set1)
# print(is_subset)


# superset = {1, 2, 3, 4, 5, 6, 7, 8}
# is_superset = superset.issuperset(set1)
# print(is_superset)


# set1.clear()
# print(set1)




#222222222222222222222222222222

# strings = ["hi", "hello", "bye", "good", "bad", "hi", "bye"]

# strings2=set(strings)
# print(strings2)

# list=list(strings2)
# print(list)



#555555555555555555555555

# set1={7,8,9,1}
# set2={9,8,2,1}

# missing2 = (set1 - set2)
# missing1 = set2-set1
# print(missing2)
# print(missing1)




#33333333333333333333333


list1 = [1,2,3,4,5,6,7,8,9]
target = 15
result = set()

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        x= target - list1[i] - list1[j]
        if x in list1[j + 1:]:
            result.add(tuple(sorted((list1[i], list1[j], x))))

print(target)
print(list(result))



#444444444444444444444444444
# words = ["listen", "silent", "enlist", "hello", "world", "cat", "tac", "elbow", "below", "state", "taste"]

# anagram = {}
# for word in words:
#     sorted1 = ''.join(sorted(word))
#     # print(sorted_word)
#     anagram.setdefault(sorted1, set()).add(word)
   

# print(list(anagram.values()))

