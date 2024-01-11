#1. WAP to declare, assign and print the string (Different ways)
#Hello World, How are you?
#i.using single quotes 'string'
#ii.using double quotes "string"
#iii.using triple quotes '''string'''
#iv.using triple double quotes """string"""
#v.using triple double quotes allows to assign (multi-line string)

'''print("Hello World, How are you?")
print('Hello World, How are you?')
print("""Hello World,
How are you?""")
print(''''''Hello World,
How are you?'''''')'''

# program to print characters from str 
'''str="hello world" 
print(str) # complete
print(str[0]) # 1st chr
print(str[1]) # 2nd chr
print(str[-1]) # last chr
print(str[-2]) # 2nd last chr
print(str[:4]) # upto 4th
print(str[:5]) # first 5
print(str[2:-1]) # 2 to 2nd last chr
for i in range(len(str)): # chr by chr
    print(str[i])'''


#  print uncommon word

'''x=input("enter ur strings ").split(" ")
flag=[]
for i in range(len(x)):
    flag.append(0)
m=""
for i in range(0,len(x)):
    for j in range(0,len(x)):
       n=0
       if  x[i]==x[j]:
            n=flag[i]+1     # try 
            # n+=1
            flag[i]=n 
sm=min(flag)
print(sm)
print(x[sm])'''

'''a = input("Enter first : ").split(" ")
b = input("Enter second : ").split(" ")

uncommon = [ ]
for i in a:
    if i not in b:
        print(i)

for i in b:
    if i not in a:
        print(i)'''

# #4
'''i = input("Enter a string to check if it's a binary string: ")

if all(bit=='0' or bit=='1' for bit in i):
    print("The entered string is a binary string.")
else:
    print("The entered string is NOT a binary string.")
        '''

# 5
'''a = input("Enter string : ")

l = []

for i in a:
    l.append(i)

l.sort()
temp = l[0]
count = 0
min = 1000000
for i in range(0,len(l),1):
    if(temp == l[i]):
        count+=1
    else:
        temp = l[i]
        index = i-1 if count < min else index
        min = count if count < min else min
        count = 1
        

print(l[index])'''

# 6
'''inpt = input("Enter string : ")

uschoice = int(input("Enter the index to remove"))
a = ''
for i in range(0,len(inpt)):
    if(not(i == uschoice)):
        a += inpt[i]

print(a)'''

# 7
'''class Employee:
    def __init__(self):
        self.s="Pankaj"
        self.id=1
        self.sex="male"
        self.city="delhi"
        self.slry=550000.00
        
        self.op=input("do you want to print employee details ").lower()
        if self.op=="yes":
            print("id     :",self.id)
            print("name   :",self.s)
            print("Gender :",self.sex)
            print("City   :",self.city)
            print("Salary :",self.slry)
e=Employee()'''



    