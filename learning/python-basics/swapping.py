string=input("enter the word\n")

first_letter= string[0]
last_letter = string [-1]

required_string = last_letter + string[1:-1] + first_letter
print(required_string)
 
