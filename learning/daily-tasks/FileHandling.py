# #Read method

# s=open("test.txt", mode='r')
# read= s.read()
# print(read)
# s.close()


#write method

# s=open("test.txt",mode="w")
# s.write("hello hai bye die")
# s.close()

# s=open("demo.txt",mode="w")
# s.write("abcsefghijklmnopqrstuvxyz")
# s.close()


#append mode

# s=open("test.txt",mode="a")
# s.write("james bond 007")
# s.close()


#r+ mode

# s=open("test.txt",mode="r+")
# print(s.read())
# s.write("hai hello")
# s.close()

#w+ mode

# s=open("test.txt",mode='w+')
# s.write("dinesh karthik")
# print(s.read())
# s.close()



# try:
#  a=int(input("enter a number\n"))
#  b=input("enter a string\n")
#  print(a+10)
#  print(b+5)
# except TypeError:
#  print("cant add two different data types")
# except ValueError:
#  print("enter a integer not string")
# finally:
#  print("programme terminated")





s= open("test.txt", mode='r')
read = s.read()
print(read)

s=open("abc.txt", mode='w')
write= s.write("hello writingg")

s=open("test.txt", mode='a')
s.write("hi hello bye")