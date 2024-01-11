# program to compute lcm of any two user input
b=int(input("enter number 1 "))
a=int(input("enter number 2 "))
if b>a:
    l=b
else:
    l=a
lcm=a*b
while l<=lcm:
    if l%a==0 and l%b==0:
        print("LCM of",a,"and",b,"=",l)
        break
    else:
        l+=1

