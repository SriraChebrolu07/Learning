number =int(input("enter factorial number\n"))
fact =1
if number<0:
 print("no factorial")

elif number == 0:
 print(1)

else :
 
 for i in range(1,number+1) :

  fact=fact*i

 print(fact)