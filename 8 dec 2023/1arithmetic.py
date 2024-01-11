# all arithmetic -> functions 
def add(a,b):
    print("sum",a+b)
def dif(a,b):
    print("difference",a-b)
def pro(a,b):
    print("product",a*b)
def div(a,b):
    print("division",a/b)
def mod(a,b):
    print("mod",a%b)
def pow(a,b):
    print("power",a**b)
def floor(a,b):
    print("floor",a//b)

c=float(input("enter num 1- "))
d=float(input("enter num 2- "))
op=input("enter your operation (\'+\',\'-\',\'X\',\'/\',\'%\',\'^\',\'//\')")
if op=="+":
    add(c,d)
elif op=="-":
    dif(c,d)
elif op=="X":
    pro(c,d)
elif op=="/":
    div(c,d)
elif op=="%":
    mod(c,d)
elif op=="^":
    pow(c,d)
elif op=="//":
    floor(c,d)    
else:
    print("invalid choice\n")