# circulate the value of n variables
n=[1,3,4,5,6]
print(n)
print('')
for i in range(len(n)):
    n.insert(len(n),n[0])
    n.pop(0)
    print(n)
