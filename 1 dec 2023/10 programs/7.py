# 7 arithmetic calculation
a=float(input("enter num 1 "))
c=input("enter first operation to perform (\"+\",\"-\",\"*\",\"/\",\"^\",\"%\",\"//\")")
b=float(input("enter num 2 "))
if c=="+":
   s=a+b
elif c=="-":
   s=a-b
elif c=="*":
   s= a*b
elif c=="/":
   s= a/b
elif c=="^":
  s= a**b
elif c=="%":
   s= a%b
elif c=="//":
  s= a//b
else:
    print("invalid operation")
d=input("enter seceond operation to perform ")
e=float(input("enter num 3 "))
if d=="+":
   print(s+e)
elif d=="-":
   print(s-e)
elif d=="*":
   print(s*e)
elif d=="/":
   print(s/e)
elif d=="^":
  print(s**e)
elif d=="%":
   print(s%e)
elif d=="//":
  print(s//e)
else:
    print("invalid operation")