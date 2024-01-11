'''# arrange list in descending order
x=[1,2,3,4,5,6]
# x.sort(reverse = True)
# print(x)
j=0
while x[j]<x[j+1]:
    for i in range(x[i]!='\0'):
        if x[i]>x[i+1]:

            swap=x[i]
            x[i]=x[i+1]
            x[i+1]=swap

    j+=1'''
l1 = []

n = int(input("enter number of elements required: "))
# creating a list using loop
for i in range(0, n):
    x = float(input())
    # appending elements to the list
    l1.append(x)
print("Original List:", l1)
# sorting in decending
for i in range(0, n):
  for j in range(0, n):
    if l1[j] <= l1[i]:
    # swapping values for arranging into descending  
      swap=l1[i]
      l1[i]=l1[j]
      l1[j]=swap  
print("Sorted List", l1)