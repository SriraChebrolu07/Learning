x=int(input("enter x\n"))
y=int(input("enter y\n"))

for i in range(x,y+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
             break
        else:
            print(i)

print(range(2,2