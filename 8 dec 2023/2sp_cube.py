# square and cube of a num
def square(a):
    j=.5
    print("square root of",a,"=",a**j)
def cube(a):
    j=1/3
    print("cube root of",a,"=",a**j)
a=int(input("enter number "))
c=input("square root(s) or cube root(c) ? ").upper()
if c=="S":
    square(a)
elif c=="C":
    cube(a)
else:
    print("invalid choice\n")