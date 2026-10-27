# #How To Create a new file Using Python
# #How To Read a File Using Python
# #How to Write(Inserting new Values) into a file
# #Delete a file

# To open a file, you use the open() function. It takes two arguments: the file name and the mode in which you want to open the file (read, write, append, etc.).

# 'r': Read (default mode). Opens the file for reading.
# 'w': Write. Opens the file for writing. If the file does not exist, it creates a new file. If the file exists, it truncates the file.
# 'a': Append. Opens the file for writing. If the file does not exist, it creates a new file. If the file exists, it appends the new data to the end of the file.
# 'b': Binary mode. Add this to the mode to open the file in binary mode (e.g., 'rb' or 'wb').




file = open("C:\Users\srira\OneDrive\Desktop\python\abc.txt",'r')
contents = file.read()
#read function takes all the data inside the file and stores it in the variable in the form of a string

print(contents)

# #readline(): Reads a single line
# file = open('/content/Python.txt','r')
# contents = file.readline()
# print(contents)

# #readlines(): It reads all the lines to a list
# file = open('/content/Python.txt','r')
# contents = file.readlines()
# print(contents)

# #Write mode in already existing file will delete all the data and enter new data
# #Write mode in New file name creates a new file and then it will enter the data
# #'W' is used to write new data into a file
# file = open("/C:\Users\srira\OneDrive\Desktop\python\xyz.txt",'w')
# file.write("Hello everyone This is how w mode works")




# ```
# # This is formatted as code
# ```



# # Writing  a string into a file
# with open("/content/Greet.txt","w") as file:
#   file.write("Hello, Students welcome to the python file handling topics!")




# 1. Opening a File in Read Mode and Reading Its Content:

# with open("/content/Words.txt",'r') as file:
#   contents =  file.read()
#   print(contents)

# file = open("/content/New_file.txt","w")
# file.write("""1. Dive into the world of programming with our Python course, designed for beginners and experienced coders alike.
# 2. Master the fundamentals of Python, from basic syntax to advanced concepts, in our comprehensive and interactive course.
# 3. Unlock the power of data manipulation and analysis as you learn to work with libraries like Pandas and NumPy in Python.
# 4. Discover the art of web development using Python frameworks like Flask and Django, creating dynamic and responsive websites.
# 5. Explore the world of artificial intelligence and machine learning, implementing algorithms and models using Python's simplicity and flexibility.
# 6. Harness Python's capabilities for automation and scripting, making repetitive tasks a thing of the past.
# 7. Gain hands-on experience through real-world projects, honing your skills in problem-solving and critical thinking.
# 8. Join a vibrant community of learners, collaborate on projects, and engage in discussions to enhance your Python proficiency.
# 9. Our expert instructors provide personalized guidance, ensuring you grasp complex topics and excel in your Python programming journey.
# 10. Enroll in our Python course today and embark on a transformative learning experience that opens doors to endless opportunities in the tech industry.
# """
# )
# file.close()

# files = open('/content/New_file.txt','w')

# files.write("The Name of the institute is level up. \n It is located in ameerpet")

# files.close()

# files = open("/content/Words.txt","r")


# import os
# os.remove("/content/Words.txt")



# file = open("/content/Python.txt","a") #append is used for updating the file
# file.write("/n11.Hello, Students welcome to the python file handling topics! ")
# file.close()

# file = open("/content/Python.txt",'r')
# contents = file.read()

# print(contents)

# with open('/content/Python.txt','a+') as file:
#   content = file.seek(1)
#   print(content)

# f_path = '/content/New_file.txt'
# new_line = '3. Printed in the middle \n'
# line_number = 2

# with open(f_path,'r') as file:
#   lines = file.readlines()
# #Converts the Content into a List

# lines.insert(line_number,new_line) #Adds the given line to a particular index of the list
# with open(f_path,'w') as file:
#   file.writelines(lines)
