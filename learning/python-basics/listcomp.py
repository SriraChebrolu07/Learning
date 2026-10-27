# a=[4,7,5,3]

# squares=[i**2 for i in a]
# print(squares)

# def squares(list1):
#     return list(map(lambda x:x**2,list1))


# print(squares([5,7,8]))

# a=10
# b=0

# try:
#     x=a/b

# except ZeroDivisionError:
#     print("numbers cant be divided by zero")

# finally:
#     print("exception handled")


# a="10"
# b=5

# try:
#     x=a+b

# except TypeError:
#     print("different datatypes cannot be added")

# finally:
#     print("exception handled type error executed")






try:
   a=int(input("enter a number\n"))
   c= a+10
   print(c)

except ValueError:
    print("enter a integer only")

finally:
    print("exception handled value error executed")