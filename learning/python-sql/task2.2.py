# 1.Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.
# 2.Write a Python program to remove duplicate words from a given string.
# 3.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string


string = input("Enter a string: ")

uppercase = 0
lowercase = 0
specialcase = 0
numeric = 0

for char in string:
    if char.isupper():
        uppercase += 1
    elif char.islower():
            lowercase += 1
    elif char.isdigit():
            numeric += 1
    else:
            specialcase += 1

print(uppercase)
print(lowercase)
print(specialcase)
print(numeric)