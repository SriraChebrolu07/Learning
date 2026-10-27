# 1.Write a Python program to find the list of words that are longer than n from a given list of words
# 2.Write a Python program to replace the last element in a list with another list.
# 3.Write a Python program to iterate over two lists simultaneously.
# --Identfy the region with lowest sales amount for the previous month and retun region and total sales amount.
#  -- region and sum sales
#  -- fileter last month
#  -- lowest sale region.


#111111111111111111111111111111111111111111

# words=["ramesh","arun","ramachandra","satish","vikram"]
# n= int(input("enter the min. length of the word:\n"))
# outputwords = list(filter(lambda i:len(i)> n,words))
# print(outputwords)




#22222222222222222222

a=[1,2,3,4,5]
b=["x","y","z"]
a.pop(-1)
print(a)
a.extend(b)
print(a)



#333333333333333333

# a=["hello","hi","bye"]
# b=[1,2,3]

# simultaneous= list(zip(a,b))
# #print(simultaneous)

# for i in simultaneous:
#     print(i)




#44444444444444444444444444444444444
    
# list=[1,2,3,4,5,6,7,8,9,10,11,12]
# list2=["a","b","c"]
# print(list)
# print(list2)

# list.append(13)
# print(list)

# list.pop(-1) 
# print(list) 

# list2.remove("a")
# print(list2)

# list.extend(list2)
# print(list)

# list2.insert(0,"a")
# print(list2)

# list2.reverse()
# print(list2)

# list3=[4,1,3,5,7,9,1,7]
# list3.sort()
# print(list3)


# list3=["a",4,"klm"]
# print(list3)
# list3.clear()
# print(list3)


# list4=["q",1,"w",2,"e",3]
# list5=[]
# list5= list4.copy()
# print(list5)