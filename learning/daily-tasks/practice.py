while True:
 word =input("enter the string to reverse\n").lower()

 rev=""

 for i in word:
    rev= i + rev
 

 if word == rev:
    print("ita a palindrome")
 else:
    print("its not a palindrome")




# class classA():
#  print("hi")

#  def display(self):
#   print("Abc")

# a=classA()
# a.display()






