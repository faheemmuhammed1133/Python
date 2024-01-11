# print pattern below
"""
A B C D E
 B C D E
  C D E
"""
x=int(input("enter the number or rows "))
for i in range(x):
    for j in range(i):
        print(" ",end="")
    for k in range(65+i,67+x):
        print(chr(k),end=" ")
    print("")