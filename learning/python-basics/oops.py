# class ClassA():
    
#    print("this is class a")
#    def fun(self):
#      print("function1")
#      a=4
#      b=6
#      print(a+b)


# obj=ClassA()
# obj.fun()







def decorator(myfunction):
 def nest():
      print("executes 1")
      myfunction()
      print("executes 2")
 return nest

@decorator
def wish():
   print("hi good mornning")