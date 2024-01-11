'''str='ITM SKILL UNIVERSITY'
print(str[-22:])
print(str[0:21])
i=0
while i<len(str): #while loop
    print(str[i])
    i+=1'''

#  find index of the letter using search 
'''def search(a,b):
    index = ""
    for i in range(0,len(a)):
        if b == a[i]:
            index = i
    
    return index

a= input("enter the word : ") 
b = input("enter the element to search : ")
index = search(a , b)
print(index) if b in a else print("Not in the word")'''

# index using find
'''str="ITM SKILLS UNIVERSITY"
print(str.find("UNIVERSITY",6,21))'''

# s in str
# str="ITM SKILLS UNIVERSITY"
# for skill in str:
#     print(skill)

'''def find(a,b):
    if b in a:
        for i in range(0,len(a)):
            flag = 0
            if(b[0] == a[i]):
                for j in range(0,len(b)):
                    if(not(a[i+j]==b[j])):
                        flag = 0
                        break
                    flag = 1
            if(flag == 1 ):
                return i
            
    else:
        return None
a= input("enter the word : ") 
b = input("enter the element to search : ")
index = find(a , b)
print(index) if b in a else print("Not in the word")'''

# print all characters of string 1,which are present in string 2:
'''def king(a,b):
    first= a.split(" ")
    second = b.split(" ")
    common = []
    for i in first:
        for j in second:
            if(i == j):
                common += [j]

    return common

print(king("""Lorem Ipsum is simply dummy text of the printing and typesetting industry
         Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
    when an unknown printer took a galley of type and scrambled it to make a type specimen 
           book""","has been writing in the paper, which is printed by printer"))'''

# compare two strings 
'''str1=input("enter the string 1 : ")
str2=input("enter the string 2 : ")

if str1 > str2:
    print(str1,"is greater than",str2)
elif str2 > str1:
    print(str2,"is greater than",str1)
else:
    print(str1,"=,str2")'''

# type  print('Hi, What\'s up?')
'''print(r"Hi,\n\t\" What's up?\"")  # r with print string as it is using \ also'''

# .format
a=input("name? ")
b=input("year ")

print("welcome {c} to itm kharghar for the year {k}".format(c=a,k=b))
print("welcome {} to itm kharghar for the year {}".format(a,b))
print("welcome {1} to itm kharghar for the year {0}".format(b,a))
