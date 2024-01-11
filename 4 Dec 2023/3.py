# dictionary cretion and modification , dictionary is key value
x={1:'zero',"to":1,'1':[3,7,8],"k":{"l":"g",1:6}}
print(x)
print(x[1])
print(x['to'])
print(x['1'])

x['1']=56
x["d"]='test'
del(x['to'])
print(x)
print(x["k"])
del(x["k"][1])
print(x['k']["l"])
print(x["k"])
