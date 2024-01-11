# number of words
'''str=input("blaablaa...")
c=1
for i in str:
    if i==" ":
        c+=1
print("number of words are",c)'''

# number of vowels
'''str=input("blaablaa...").upper()
c=0
for i in str:
    if i =="A" or i =="E" or i =="I" or i =="O" or i =="U":
        c+=1
print("number of vowels are",c)'''

# anagram
'''
value="false"
if len(str1)==len(str2):
    for i in range(len(str1)):
        for j in  range(len(str2)):
            if str1[i] in str2[j]:
                value="true"
if value=="true":
    
    print("both are anogram")
else:
    print("no anogram")'''
'''a = input("Enter first : ")
b = input("Enter second : ")

flag = 1
for k in b:
    if not(k in a):

        flag = 0
        break

    count = 0
    for i in a:
        if(i == k):
            count+=1
    
    for i in b:
        if(k == i ):
            count-=1

    if(count == 0):
        flag = 1
    else:
        flag = 0

    
        

if flag == 0:
    print("No")
else:
    print("YES")'''

'''str1= input("Enter first : ")
str2 = input("Enter second : ")
a=sorted(str1)
b=sorted(str2)
if a==b:
    print("anogram")
else:
    print("no")'''

# camelCase - snake_case
'''a = input("Enter  : ").split(" ")
for i in range(0,len(a)):
    str1 = ""
    for j in range(0,len(a[i])):
        
        if(a[i][j] == a[i][j].upper()):
            if(j == 0):
                str1 += a[i][j]
            else:
                str1 += "_" + a[i][j].lower()
        else:
            str1 += a[i][j]
    
    a[i] = str1


for i in a:
    print(i,end=" ")'''

# sort the list of string according to length

'''
'''
 
a = input("enter : ").split(" ")

print(a)

for i in range(0,len(a)):
    for j in range(i,len(a)):

        if(len(a[i]) > len(a[j])):
            temp = a[j]
            a[j] = a[i]
            a[i] = temp

for i in a:
    print(i,end=" ")