# multi-D list methods
subl=[1,'hello',[1,2]]
l=[[0,-1,-3,["a",2,subl]],[1,2,8],[9,0,-4,"c","@"]] # we can have differnt length,different datatype,etc..
print(l)
print(l[0])
print(l[0][2])
print(l[0][3][0])
# printint a value from sublist
print(l[0][3][2][1])

# printing the sublist nested list
print(l[0][3][2])
# printing the length of sublist
print(len(l[0][3][2]))

#  printing the sublist nested list's sublist
print(l[0][3][2][2])
# printint the sublist nested list's sublist's value
print(l[0][3][2][2][0])
# printing the length of sublist
print(len(l[0][3][2][2]))


