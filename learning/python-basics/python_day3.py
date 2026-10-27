a="kingsman"
b="546"
c=786
d="18Kohli"

print(a.isdigit())
print(c.isdigit())
print(b.isdigit())
print(d.isdigit())



e = "welcome to levelup training"
print(len(e))

print(e.strip())

print(e.lstrip())
print(e.rstrip())

print(e.capitalize())

f="The INNER JOIN keyword selects all rows from both the tables as long as the condition is satisfied."

print(f.split())
print(f.split(" "))
print(f.split("as"))

print(f.count('a'))
print(f.count("  "))

word = "hello"

print(word.center(11,' '))
print(word.center(21,'m'))

print(f.index('k'))


k=int(input("enter the value of k\n"))
result=500/k
print(result)

n=input("Enter a number for n or press x to end the programme")
if n=="x":
    print("programme terminated")
elif n.isdigit():
    x == int(n)

result=1000/n
print(result)


p="python is versatile"

print(p.isdigit())
print(p.isalpha())
print(p.isalnum())

q=117
#print(q.isalpha())
#print(q.isalnum())

y="Python is much simpler and easier than Java"

print(y.replace("Java", "Core Java"))