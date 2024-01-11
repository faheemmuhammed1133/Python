# particular value's index or it's indices
listnum=[1,2,1,4,5,6,7,8,9]
liststr=["a","a","b","c","d"]
ln=len(listnum)
ls=len(liststr)
print(liststr,listnum)
freq=0
ind=[]
choose=int(input("enter 1 for checking the \'numbers\' 2 for checking \'string\' "))
if  choose ==2:
    j=input("enter the value to find index ")
    for i in range(ls):
        if j==liststr[i]:
            freq+=1
            ind+=[i]
    print(ind,"indices/index of string",j)
    print(freq,"frequency of",j)
else:
    j=int(input("enter the value to find index "))
    for i in range(ln):
        if j==listnum[i]:
            freq+=1
            ind+=[i]
    print(ind,"indices/index of num",j)
    print(freq,"frequency of",j)