"""
A
BB
CCC
DDDD
"""
n=int(input('enter the range '))
x='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(n):
    for j in range(i+1):
        print(x[i],end="")
    print(" ")