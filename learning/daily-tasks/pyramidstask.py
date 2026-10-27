#How to create a pyramids in Python?
# Different types of pyramids:
# 1.simple pyramid,leftside,Rightside pyramids.
# 2.inverted pyramid
# 3.Number pyramid
# 4.floyd's Trinagle pyramid
# 5.Daimond shape pyramid


#Build a program that generates a word cloud from a given text.



#normal pyramid

# rows = int(input("Enter the no. of pyramid rows required\n"))
# for i in range(rows):
#     print(i)
#     print(" " * (rows - i - 1) + "*" * (2 * i + 1))



# #right pyramid

# rows=int(input("enter no. of rows\n"))
# for i in range(rows):
#     print("*" * (i + 1))


#left pyramid

# rows=int(input("enter no. of rows\n"))
# for i in range(rows):
#     print(" " * (rows - i - 1) + "*" * (i + 1))



#inverted pyramid


# rows=int(input("enter no. of rows\n"))
# for i in range(rows, 0, -1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))

 
#diamond pyramid

# rows=int(input("enter no. of rows\n"))
# for i in range(rows):
#     print(" " * (rows - i - 1) + "*" * (2 * i + 1))

# for i in range(rows - 2, -1, -1):
#     print(" " * (rows - i - 1) + "*" * (2 * i + 1))


#number pyramid


rows=int(input("enter no. of rows\n"))
for i in range(1, rows + 1):
  
    print(" " * (rows - i), end="")
    
    
    for j in range(1, i + 1):
        print(j, end=" ")
    
   
    print()
