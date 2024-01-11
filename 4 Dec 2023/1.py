'''# x=[1,"hello",(3+2j)]
# print(x)

# print(x[1])

# print(x[-4:2])

# print(x[2])

# print(x[0])
# list and modify list '''
x=[2,5,7,"+"]
y=x
x[2]=12
# print(x)
x.append(34)
y.append(9)
print(y)
z=x.append(34)
print(z==None)
print(z)
x=x+[1,3]
y=x
print(x)
print(y)