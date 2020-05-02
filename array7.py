rnumbers=[]
items=[]
print("enter a number, press x to stop")
i=input()
while(i != str("x")):
    print("enter a number")
    items.append(i) 
    i=input()
items.sort()
a=1
c=-1
d=0
while(a < (len(items))):
    c=c+1
    d=d+1
    if items[c]==items[d]:
        rnumbers.append(items[c])
    a=a+1
print("repeating numbers: ", rnumbers)