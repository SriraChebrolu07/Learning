# file = open(r"C:\Users\srira\OneDrive\Desktop\python\abc.txt")
# contents = file.read()
# #read function takes all the data inside the file and stores it in the variable in the form of a string

# print(contents)


# file = open("C:\Users\srira\OneDrive\Desktop\python\abc.txt","w")
# file.write("See you soon!")
# file.close()



# file = open(r"C:\Users\srira\OneDrive\Desktop\python\abc.txt")
# contents = file.read()
# #read function takes all the data inside the file and stores it in the variable in the form of a string

# print(contents)


# file=open("abc.txt","a")
# file.write("appending done")
# file.close()

# file = open("abc.txt","w")
# file.write("hello abc, writing doone\n hello world")
# file.close()

# file=open("abc.txt","r")
# contents = file.read(10)
# print(contents)

file = open("C:\\Users\\srira\\OneDrive\\Desktop\\excel2.csv","r")
contents = file.read()
print(contents)

# file=open("C:\\Users\\srira\\OneDrive\\Desktop\\Book1.csv","w")
# file.write("harsha priya is a professional python coder")
# file.close()

# file=open("C:\\Users\\srira\\OneDrive\\Desktop\\Book1.csv","a")
# file.write("\n harsha priya ye no.1 inka evari valla kadhu")
# file.close()

file=open("C:\\Users\\srira\\OneDrive\\Desktop\\excel2.csv","w")
file.write("hello sudarshan sp")
file.close()


import os
os.remove("location")