# 1.Write a Python program to find the least common multiple (LCM) of two positive integers.
# 2.Write a Python program that removes and prints every third number from a list of numbers until the list is empty.
#  3.Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations.

 #Sample data:
# /*
# X = [10, 20, 20, 20]
# Y = [10, 20, 30, 40]
# Z = [10, 30, 40, 20]
# target = 70
# */
#4.Write a Python program that accepts a filename from the user and prints the extension of the file.



#11111111111111111111111111111111111111111111


# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# # Finding the maximum of the two numbers
# max_num = max(num1, num2)

# # Checking for the first common multiple
# while True:
#     if max_num % num1 == 0 and max_num % num2 == 0:
#         lcm = max_num
#         break
#     max_num += 1


# print(lcm)



#22222222222222222222222222222222222

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #def remove_every_third(numbers):
# while numbers:
#         index_to_remove = (len(numbers) + 2) // 3 - 1  # Index of the third element
#         if index_to_remove >= len(numbers):
#             index_to_remove = len(numbers) - 1
#         removed_number = numbers.pop(index_to_remove)  # Remove the third element
#         print("Removed:", removed_number)

# print(numbers)




#444444444444
name = input("enter the filename with extension\n")
y= name.split(".")
print("."+y[-1])
