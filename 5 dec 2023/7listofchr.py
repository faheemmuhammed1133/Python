# program to add first characters of words in a lisrt to another list
l1 = input("enter the words of list: ").split()

j=[]
for i in range(0,len(l1)):
    j.append(l1[i][0])
print(j)