# # '.' : it matches any character except newline
import re
pattern = r"A....."
name = input('Enter the string value  ')
result = re.search(pattern,name,flags = re.IGNORECASE)
print(result.group())

# import re
# pattern = r"A....."
# my_string = 'animal Kingdom'
# result = re.search(pattern,my_string,flags = re.I)
# result.group()






# a = r'+^'
# type(re)
# a = "This is the first line.This is the Second line"
# print(a)






# #'^' : It makes sure that the given pattern is at the start of the string
# #'^' will always be written in the starting of the pattern

# import re
# pattern = r"^Hello"
# text = "Hello Python"
# result = re.search(pattern,text,re.I)
# result.group()

# import re
# pattern = r"^9........."
# number = '958674893'
# result = re.search(pattern,number)
# result.group()





# #'$' : It makes sure that the given pattern is at the end of the string
# #'$' symbol always comes in the last of the pattern

# import re
# pattern = r"Thankyou$"
# text = "Hello students welcome to this topic thankyou"
# result = re.search(pattern,text,flags = re.I)
# result

# #"*" : matches 0 or more(Infinite) occurences of the preceding(Before *) character
# #"*" means the preceding character is optional
# import re
# pattern = r"xy*" # is the same as x*y*
# result = re.search(pattern,"x",flags = re.I)
# print(result.group())





 #"+" : matches 1 or more(Infinite) occurences of the preceding character
 #"+" : Means the Preceding Character is mandatory but it can be repeated n number of times

# import re
# pattern = r"xy+"
# result = re.search(pattern,"x")
# print(result.group())

# #"?" : matches 0 occurences or 1 of preceding character
# #"*" : matches 0 occurrences and multiple occurences
# # import re
# # pattern = r"xy?"
# # result = re.search(pattern,"xyyyyyyyyyyyy")
# # print(result.group())



