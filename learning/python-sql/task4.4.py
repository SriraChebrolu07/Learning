# List Advanced:
# 1.Write a Python function to sort a list of dictionaries based on values of a key.
# 2.Write a Python a function to find the union and intersection of two lists.
# 3.Write a Python function to find the kth smallest and largest element in a list.

# SQL:
# 1.which metro city had the highest number of restrent orders in january 2024?
# write the sql query to retrieve the city name and the total count of orders,ordered by the total count of order in decending order?

#111111111111111
def sortlist(list, key):
    return sorted(list, key=lambda x: x[key])

list1 = [{"age":1},{"age":5},{"age":3},{"age":2},{"age":4}]

sorted_list = sortlist(list1, 'age')
print(sorted_list)




#22222222222222

# def UI(L1,L2):
#  union = list(set(L1+L2))
#  Intersection= list(set(L1) & set(L2))

#  return union, Intersection

# L1=[1,2,2,3,4]
# L2=[4,5,5,5]

# union = UI(L1, L2)
# intersection = UI(L1, L2)
# print( union)
# print( intersection)



#333333333333333333333333333

# list1= [5,2,3,1,4,6]
# def nthSL(list):

# #  list1= [5,2,3,1,4,6]
#  list1.sort()
#  #print(list)
#  n=int(input("enter the n value:\n"))
#  nth_smallest = list1[n-1]
#  nth_largest= list1[-n]
#  print(nth_smallest)
#  print(nth_largest)

# nthSL(list1)



# list= [5,2,3,1,4,6]
# list.sort()
# print(list)
# n=int(input("enter the n value:\n"))
# nth_smallest = list[n-1]
# nth_largest= list[-n]
# print(nth_smallest)
# print(nth_largest)



# a=[1,2,3,4,5,6,7,8,9]

# print(a[0])
# print[a[-1]]




# {'name': 'Charlie', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
# def sort_list_of_dicts(list_of_dicts, key):
#     return sorted(list_of_dicts, key=lambda x: x[key])

# list_of_dicts = [
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 30},
#     {'name': 'Charlie', 'age': 20}
# ]

# sorted_list = sort_list_of_dicts(list_of_dicts, 'age')
# print(sorted_list)









# def UI(list1,list2):
#  union = list(set(list1+list2))
#  intersection =list(set(list1) & set(list2))
# #  return union, intersection
 

#  print(union)
#  print(intersection)

# L1=[1,2,2,3,3]
# L2=[2,2,3,3,3,4]
# UI(L1,L2)