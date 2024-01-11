# copy dictionaries and lists
# list
print('list')
l1=[4]
l2=list(l1)
l1[0]=44
print(l1)
print(l2)
# dictionary
print('dictionary')
d={1:"abc"}
d2=d.copy()
d[1]="xyz"
print(d)
print(d2)