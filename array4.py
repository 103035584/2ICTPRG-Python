def fullname(str1):
   lst = str1.split()
   print(lst)
   newspace = ""
   for i in range(len(lst)):
      str1 = lst[i]
      newspace += (str1[0].upper())
   return newspace 
str1=input("Full Name :")
print("initials :",fullname(str1))  