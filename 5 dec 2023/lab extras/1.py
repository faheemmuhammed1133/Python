# wap to declare and print a list number list
'''l1=[1,2,3,4,5,6,7,8,10,9]
print("elements in list",l1)
print("list elements are:")
for i in range(len(l1)):
    print("elements ",i,"in list",l1[i])'''
#  string list
'''l2=["BMW","Daimler AG","Volks Wagon","Aston Martin"]
print("elements in list",l2)
print("list elements are:")
for i in range(len(l2)):
    print("elements ",i,"in list",l2[i])'''
#  heterogeniuos list
'''l3=["BMW","Daimler AG",1,3]
print("elements in list",l3)
print("list elements are:")
for i in range(len(l3)):
    print("elements ",i,"in list",l3[i])'''
# WAP for various operation 
'''l4=[10,20,30,40,50,70,60,80,90,100]
print(l4)
print(l4[0])
print("4th element",l4[3])
# 0 to 4th element 
print("o to 4th element",l4[:4])

# print list -7 or 3rd element
print(l4[-7 and 3])
l4.append(111)
print("og list",l4)
l4.sort()
print("after sorting",l4)
l4.pop()
print("after poping",l4)
#  remove specified item
l4.remove(80)
print("after removing 80",l4)
#  entering an element in specified index
l4.insert(2,100)
print("after inserting 100",l4)
#  counting the occurance of 100/specific element
print(l4.count(100))
#  extend an element in a list
l4.extend([120,110])
l4+=[120,110]
print("after extending",l4)
# reversing the list
l4.reverse()
print("after reversing",l4)'''
# wAp to create 2 list with even numbers and odd number from list
'''ls=[11,22,33,44,55]
even=[]
odd=[]
for i in range(len(ls)):
    if ls[i]%2==0:
        even+=[ls[i]]
    else:
        odd+=[ls[i]]
print("even numbers",even)
print("odd number",odd)'''
# wap iterate / traverse a list in reverse order by using reverse,slicing,insert method
'''l=[10,20,30,40,50,60]
l.reverse()
print("using reverse",l)
# slicing
print("slice",l[::-1])
# insert reverse
l=[10,20,30,40,50,60]
print("reverse [",end='')
for i in range(len(l)):
    print(l[len(l)-i-1],end=",")
print("]")
'''

# wap extend a list in python from 10 to 15 by using append ,+,extend
'''a=[]
p=[]
e=[]
for i in range(10,151,10):
    a.append(i)
    p+=[i]
    e.extend([i])
print("append:",a) 
print("+     :",p) 
print("extend:",e) '''
# wap to find sum and mean
'''l=[1,2,3,4,5,6,7,8,9,10]
print(l)
sum=0
for i in range (len(l)):
    sum+=l[i]
print("sum of list",sum)
print("mean:",sum/len(l))'''
# wap to remove all duplicate value in list
'''l=[1,2,3,4,2,3,4,5,6,7,8,3,6,0]
a=[]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i] not in a:
            a.extend([l[i]])
print(a)'''

#  add to matrices
'''x=[[2,5,4],[1,3,9],[7,6,2]]
y=[[1,8,5],[7,3,6],[4,0,8]]
r=[[1,2,3],[2,3,4],[3,4,5]]
for i in range(len(x)):
    for j in range(len(x)):
        r[i][j]=x[i][j]+y[i][j]
    print(r[i])'''