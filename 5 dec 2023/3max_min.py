# WAp to find the smallest and the largest number in the list
x=[]
n=int(input("enter the length of list "))
# getting input to list
for i in range(0,n):
    k=float(input())
    x.append(k)
print("Your list",x)
# sorting in ascendig order to get things easier to get max and min
for i in range(n):
    for j in range(n):
        if x[i]>=x[j]:
            swap=x[i]
            x[i]=x[j]
            x[j]=swap
print("sorted list",x)
# printing the smallest and largest 
print("smallest element in list",x[n-1])
print("largest element in list",x[0])