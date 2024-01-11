b=int(input("enter number 1 "))
a=int(input("enter number 2 "))
if b>a:
    lcm=b
else:
    lcm=a
l=a*b
while lcm<=l:
    if lcm%a==0 and lcm%b==0:
        # print("LCM of",a,"and",b,"=",lcm)
        break
    else:
        lcm+=1
print("hcf =",(l/lcm))
