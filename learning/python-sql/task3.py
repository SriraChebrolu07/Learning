# fruits = ["litci", "apple", "cherry", "coconut","banana"]

# fruitsA = []

# for fruit in fruits:
#     if "a" in fruit:
#         fruitsA.append(fruit)

# print(fruitsA)




def evennumber():
    num=0
    while True:
     yield num 
     num=num+2

y= evennumber()


print(next(y))


