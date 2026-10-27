# a="hello world"
# count=0
# word="AEIOU"
# for x in a:
#   if x ==" ":
#     break
#   if x.upper() in word:
#       count+=1
# print(count)

# #-------------------------------------------------------------------


# word = "python and other programming languages"
# vowel_count=0
# vowels= "aeiou"
# for i in word:
#    if i.lower() in vowels:
#       vowel_count+=1
# print(vowel_count)

#------------------------------------------------------------------


# n=6
# for i in range(1,11):
#    print(f'{n}x{i}=',n*i)


#------------------------------------------------------------------

# names=["as","df","gh"]
# for i in names:
#  print("hello",i,"!")



#----------------------------------------------
# n=int(input("enter the upper limit number\n"))
# i=1
# sum_result = 0
# for i in range(1, n):
#     sum_result += i

# print("Sum:", sum_result)

 
d={}
d['name']="lucy"
d['team']="a team"
d["country"]="USA"

print(d)
d.items()
print(d.items())

for i,j in d.items():
   print(f'keyname={i},value={j}')



# list=["asdf", "qwer","zxcv"]
# for i in list:
#    print(i)