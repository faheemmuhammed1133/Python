# print pattern 
"""
  C D E
 B C D E 
A B C D E 
 B C D E 
  C D E
x-3
x-3-i
65+i,67+x
x-2
"""
# x=int(input("enter the number or rows "))
x=5
for i in range(x-3):
    for j in range(2-i,0,-1):
        print(" ",end="")
    for k in range(70-3-i,67+x-2):
        print(chr(k),end=" ")
    print("")
for i in range(0,x-2):
    for j in range(i):
        print(" ",end="")
    for k in range(65+i,67+x-2):
        print(chr(k),end=" ")
    print("")