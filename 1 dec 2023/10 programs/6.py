# 6 largest among three
a=(input("enter num 1 "))
b=(input("enter num 2 "))
c=(input("enter num 3 "))
if a!=(float or int) or b!=(float or int) or c!=(float or int):
  print("invalid input")
else:
  if a>b and a>c:
    print(a,"greater than",b,"and",c)
  elif b>a and b>c:
    print(b,"greater than",a,"and",c)
  else:
    print(c,"greater than",b,"and",a)