# 1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
# 2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
# 3.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
# 4.Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
# 5.Write a Python function to reverse a list at a specific location.


# #11111111

# num1 = int(input("enter a number i.e., numenator\n"))
# num2 = int(input("enter a number i.e., denominator\n"))

# try:
#  print(num1/num2)

# except ZeroDivisionError:
#   print("denominator cannot be zero, enter a natural number")

# finally:
#  print("programme terminated")


 #2222222

# try:
#  num1 = int(input("enter a number\n"))
#  num2 = int(input("enter a second number\n"))
#  print(num1+num2)

# except ValueError:
#  print("enter a number not word")

# finally:
#  print("programme terminated")

 




#333333333333333333333
# try:
#  a= input("enter the first number/string\n")
#  b= int(input("enter the second number\n"))
#  print(a+b)

# except TypeError:
#   print("cant take two different data types, please enter numberes only")



#4444444444444444444444444444444
  

# try:
#  x= int(input("enter x value\n"))
#  y= int(input("enter y value\n"))
#  print(x/y)

# except ArithmeticError as error:
#  print(error)


 
#55555555555555555555555555555
 
a=[1,2,3,4,5,6,7,8,9,10,11,12]
i= int(input("enter the location\n"))
if i>len(a) and i<0:
    print("please enter the index in lists range")
else:

# print(a[::3]) #prints every 3rd number
# print(a[:3]) #prints 0 to 2 index
# print(a[3:]) #prints from 3rd index to end

 b=a[i:]
 print(b)
 b.reverse()
 print(b)
 c=a[:i]
#print(c)
#print(b)
 print(c+b)








# #66666666

# try:
#     a= input("enter a string/number\n")
#     b= int(input("enter 2nd number b\n"))
#     print(a+b)
# except ValueError:
#     print("enter the integer not strings")

# except TypeError:
#     print("cant add two different datatypes")

# finally:
#     ("errors handled and loop terminated")
