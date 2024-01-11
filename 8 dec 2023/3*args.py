# *args use case
'''def fc(*args):
    for i in args:
        print(i,end=" ")
fc(1,2,3,5,7,8,9,90)
print()'''
# def add(a):
#     sum=0
#     sum+=a
'''def fnct(*args):
    sum=0
    for i in args:
        print(i)
    for j in args:
        sum+=j
    print("sum of all values passed is",sum)

l=[]
n=1
while n!=0:
    n=int(input("enter a number (-1.1 to exit )"))
    if n!=0:
        l.append(n)
fnct(l)'''

# function(a,b,*args) -> function(a=8,b=4,2,3,4,6)
'''def fnct(a,b,*args):
    print(a,b)
    print(args)
fnct(1,3,2,a=4,b=5)'''

# keywords based arguments   **kwargs
'''def kwfnc(**kwargs):
    print(kwargs)
kwfnc(otp="456d4")'''

# both
'''def fnct(*args,**kwargs):
    for i in range(len(args)):
        print(i,"=",args[i])
    for i in kwargs:
        print(i,"=",kwargs[i])
fnct("hello","itm",name="abc",age=13)'''

# question and answer
'''def welcome(n):
    print("_________welcome________")
    print(n)
    print("to ITM SKILLS UNIVERSIY ")
welcome("Jeevan Naidu")'''

# welcome details:
'''import random
def greet(**kwargs):
    print("")
    for i in kwargs:
        print(i,":",kwargs[i])
    print("")

n=input("enter your name ")
a=int(input("enter your age "))
e=input("enter your email ")
# r=int(input("enter your roll no "))
r=random.randint(0,100)
greet(Name=n,Age=a,Email=e,RollNo=r)'''

# user choice
import random
# std={}
def greet(k):
    for i in k:
        print(i,":",k[i])
d={}
choice=input("Do you want to enter Name ")
if choice=="yes":
    name=input("What is your name ")
    d["Name"]=name
choice=input("Do you want to provide your Age ")
if choice=="yes":
    age=int(input("How old are you "))
    d["Age"]=age
choice=input("Do you want to provide your email ")
if choice=="yes":
    email=input("Enter Your Email ")
    d["Eame"]=email
rollno=random.randint(1,46)
d["Roll No"]=rollno
greet(d)


