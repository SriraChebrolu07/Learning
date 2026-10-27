# def myfun(*args):
#     for x in args:
#         print(x)

# print(myfun("hi",1,2,3))



# def addnumbers(*args):
#     result =0
#     for num in args:
#         result=result+sum
#         return result
    
#     print(addnumbers(1,2,3))


# def concatestr(*args):
#     result=""
#     for str in args:
#         result=result+str
#         return result
    
# print(concatestr("hi","good morning"))




def calavg(*args):
    if len(args)==0:
      return 0
    return sum(args)/len(args)

print(calavg(1,2,3))