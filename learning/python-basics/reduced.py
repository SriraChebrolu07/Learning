from functools  import reduce
def square(x):
    return x**2
numbers=[1,2,3,4,5]
squared = list(map(square,numbers))
sum= reduce(lambda x,y:x+y,squared)

print(sum)