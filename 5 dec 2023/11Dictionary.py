# common methods in dictionaries
x={1:'zero',"to":1,'1':[3,7,8]}
y={"z":"r"}
# all keys
print(x.keys())
# all values
print(x.values())
# clear the dictionary
x.clear()

x.update(y) # overwrites any matching key in x by y 
print(x)