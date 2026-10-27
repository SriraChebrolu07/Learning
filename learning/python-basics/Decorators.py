#Procedural Programming
#Step By Step Instructions

#Treating Functions As Objects
def square(a):
  return a**2

s = square

s(2)

#A python function can be used as input parameter/arguments of a different function
def shout(a):
  return a.upper()

def whisper(a):
  return a.lower()

def greet(func):
  greeting = func("Hello Students welcome to Python Class")
  print(greeting)

greet(shout)

greet(whisper)

def Outer (x):
  def Inner(y):
    return x+y
  return Inner

c = Outer(51000)

c(50000)

#Function can return another function by accessing the input parameters of other functions
def Outer(x,y):
  def Inner(a,b):
    return x+y+a+b
  return Inner

a = Outer(200,200)

a(100,100)

#Decorator is also called as a Wrapper Function
#If you want to modify the behaviour of the function without changing the actual the function

def div(a,b):
  return a/b

def sub(a,b):
  return a-b

sub(4,2)

div(4,2)

div(2,4)

def smart_div(func):
  def inner(a,b):
    if b>a:
      a,b = b,a
    return func(a,b)

  return inner



div = smart_div(div)

div(2,10)

div(10,2)

sub = smart_div(sub)

sub(2,4)

sub(4,2)

def hello_decorator(func):

	def inner1():
		print("Before")


		func()

		print("After")

	return inner1


def function_to_be_used():
	print("Inside")


function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()


def greet():
  print('Hello This is Inside the function')

greet()

my_decorator(greet)