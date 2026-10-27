# word=input("enter a word/sentence\n")

# word1 = word.lower().replace(" ", "")

# if word1[::1] == word1[::-1]:
#     print("its a palimdrome")

# else:
#     print("not a palindrome")

# str= input("enter a sentense\n")

# str1 = str.lower().replace(" ", "")

# if str1[::1] == str1[::-1]:
#     print("its a palindrome")
# else:
#     print("not a palindrome")

#binary search



# lista = [5,7,9,3,8,4]

# def binary(lista,high,low,x):
#     if high != low:
#         mid = (high + low)//2
#         if mid == x:
#          return mid
#     elif x > mid:
        



# a = 'python'

# for i in a:
#     print(i)

# b = 'java'

# for i in b:
#     print(i,end=" ")







# a=input("Enter a name or number\n")
# print(a[::-1])

# if a.lower() == a[::-1].lower():
#     print("its a palindrome")

# else:
#     print("not a palindrome")







# for i in range(10):
    
#     if i==5:
#         break
#     print(i,end=" ")


# i=0
# while i <=10:
#     print(i, end=" ")
#     if i==5:
#         break
#     i=i+1




# n= int(input("enter the table you want"))

# for i in range(1,11):
#     print(i)
#     i=i+n





# n=int(input("enter the table you want\n"))

# def genmul(n):
#  for i in range(1,11):
#   yield f'{n}*{i}= {n*i}'


# y = genmul(n)


# print(next(y))







# n= int(input("enter the upper limit\n"))
# def genodd():
#  for i in range(1,n):
#   if i%2==1:
#    yield i**2

# y = genodd()

# for j in y:
#  print(j)









# n= int(input("no: "))
# count=0
# i=2
# while(i*i<=n):
#   if n%i==0:
#     count+=1
#   i+=1
# if count==1:
#  print("not prime", n)
# else:
#  print("prime",n)
  



# import re

# pattern = r"as......."
# source=input("enter the string\n")

# result=re.search(pattern,source, flags=re.I)

# print(result.group())


# class parent:
#     print("parent class")
#     def a(self):
#         print("fun a")

# class child(parent):
#     def b(self):
#         print('this is b from child')

# obj=child()

# obj.a()



# class median:
#     def func(self):
#      list=[5,4,9,3,7,5,4]

#      list.sort()
#      n=len(list)
#      mid= n/2
#      if len(list)%2==1:
#        print(list(n/2))
#      elif:
#       print(list((mid-1)/2)+mid/2)
#      else:
#       print('numbers only')


# ob=median()
# ob.func()



# import array

# myarray = array.array(1,5,7,9)

# print(myarray)




# import numpy as np

# myarray=np.array([1,5,7,8,9])

# print(myarray)




# #bank account using oops

# class Bank:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance=balance

#     def deposit(self,deposit_amount):
#         self.deposit_amount=deposit_amount
#         if deposit_amount>0:
#             self.balance=self.balance + deposit_amount
#             print(f"sucessfully deposited  {deposit_amount}  ,balance is {self.balance}")

#         else:
#             print("enter a valid amount to deposit")

#     def withdrawal(self,withdrawal_amount):
#         self.withdrawal_amount=withdrawal_amount

#         if withdrawal_amount < self.balance:
#             self.balance=self.balance-withdrawal_amount

#             print(f"amount withdrawn, balance is {self.balance}")

#         else:
#             print("insufficient balance")


# object=Bank('chandrasekhar',120000)
# object.deposit(5000)
# object.withdrawal(2000)


# amount=25

# print("we have amount")
# print(f"we have {amount}")
# print("testinfg{amount}")


# import math

# n = math.ceil(11.70 / 3)
# print(n) 




# a= int(input("Enter a number to check even number or not\n"))
# if a%2==0:
#     print("even ")
# else:
#     print("not even")



# b= int(input("Enter a number to check odd number or not\n"))
# if b%2==1:
#     print("odd")
# else:
#     print("not odd")


# c=int(input("enter a number to check prime"))

# count_divisors=0

# if c==1:
#  print("its not a prime")

# elif c==2:
#     print("its  a prime")

# while c*2.5 <= c//2:
# #    count_divisors = count_divisors +1





# n=int(input("enter number\n"))
# factorial =1

# for i in range(1,n+1):
    
#     factorial*=i

# print(factorial)



# def fac(n):
#    if n==1:
#       return 1
#    return n*fac(n-1)

# print(fac(5))

# n =int(input("enter n"))


# l = [5,4,71,68,94,2,9]
# m = min(l)
# flag = True
# while(flag):
#     if m+1 not in l:
#         print(m+1)
#         flag =False
#     m+=1



# def add(*args):
#     return sum(args)

# print(add(5,4,6))


n= int(input("enter the number to check\n"))
if n<2:
     print("not a prime number")

else:
 for i in range(2, int(n**0.5)+1):
    if n%i == 0:
     print("not a prime number")
     break
 else:
       print(" a prime number")