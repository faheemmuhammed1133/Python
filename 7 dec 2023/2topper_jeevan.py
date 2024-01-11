# wap that creates cubes of odd number in the range 1-10
'''d={}
for i in range(1,10,2):
    d[i]=i**3
print(d)'''

# (nested tuple) wap to print name of the topper,from the list of 4 people, and his/her marks in 4 subjects 
# were in the marks are specified as a list in the tupple topper
mark=[]
name=[]
students=[]
for i in range(4):
    n=input("enter the name ")
    name.append(n)
    for j in range(4):
        m=float(input("enter mark in sub"))
        mark.append(m)
for i in range(4):
    students+=[(name[i],tuple(mark[i*4:i*4+4]))]
# ,tuple(mark)
# print(tuple(students))
total=[0,0,0,0]
k=1
for i in range(4):
    for j in range(i*4,4*k):
        total[i]+=mark[j]
    k+=1
# print(total)
topper=[]
# maxi=0
maxi=total.index(max(total))
# for  i in range(4):
#     for j in range(4):
#         if total[j]>total[i]:
#             maxi=j
topper.append(name[maxi])
topper.append(tuple(mark[maxi*4:maxi*4+4]))

print(tuple(topper),", Topper !")