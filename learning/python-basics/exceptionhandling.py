# print('10'+10)

# try:
#   c = 10+'20'
# except TypeError:
#   print('you cannot add two different Datatypes')
# else:
#   print(c)
# finally:
#   print('The Program has ended')





# print(10/0)

# print(n)

# try:#Contains the code that might raise an error, if no errors it will execute normally if there are errors then it pushes the code to except if no errors it will push to else
#   print(r)
# except NameError:
#   print('There is no variable called r Please create and assign value')
# finally:#It Always executes and it always executes in the last
#   print('The Program has ended')

# #To Handle Errors Gracefully in a way that the users will understand
# #To create a robust and a user friendly code we will be using error handling by try and except block


# print('M'*10)


# try:
#   num = int(input("Enter Numerator"))
#   deno = int(input("Enter Denominator"))
#   d = num/deno
# except ValueError:
#   print('Please Enter only Integers')
# except ZeroDivisionError:
#   print('Denominator Cannot Be Zero')
# else:
#   print(d)
# finally:
#   print('.........')



# try:
#   a = int(input('Enter A Value'))
# except ValueError:
#   print('Please enter only Integers')
# else:
#   print(a)
# finally:
#   print('Thanks')

# L1 =

# L1[8]

# L2 = [1,2,3,4,5]
# try:
#   index = int(input('enter a number for index: '))
#   c = L2[index]
# except NameError:
#     print('The Variable is Not Initialized')
# except ValueError:
#   print('Please enter only numbers')
# except IndexError:
#   print('Please enter the correct index.Index unavailable')
# else:
#   print(c)
# finally:
#   print('End')



# d1 = {'a':100,'b':'200'}

# d1['a']

# try:
#   key = input("Enter a KeyName")
#   c = d1[f'{key}']
# except KeyError:
#   print('The Given KeyName is Not available in the dictionary')
# except NameError:
#   print('There is no variable of that name  please check the code')
# else:
#   print(c)
# finally:
#   print('Program has ended')

# try:
#   print(10/0)
# except Exception as a:
#   print(a.args)