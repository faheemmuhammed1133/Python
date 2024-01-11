# 10  first n natural numbers and there sum
n=int(input("enter the range of natural number "))
s=1
print(s,end="")
for i in range(2,n+1):
  s+=i
  print(" +",i,end="")

print(" =",s)