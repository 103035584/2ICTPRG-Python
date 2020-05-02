print("hello")
sum=0.0
num=(input('enter some numbers (press x to stop)'))
while(num != str("x")):
    sum=sum + int(num)
    num=(input('enter some numbers (press x to stop)'))
    num=str(num)
print("the sume is " + str(sum))