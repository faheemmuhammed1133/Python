# 8 leap year or not
x=int(input("enter an year to check "))
if (x%4==0 and x%100!=0) or x%400==0:
  print(x,"is a leap year")
else:
  print(x,"not a leap year")