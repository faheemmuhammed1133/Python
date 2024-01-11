# print pattern
"""
 *
 **
 ***
 ****
 *****
n=int(input("enter the range"))
for i in range(n):
    for j in range(i+1):
        print("*",end = "")
    
    print("")
"""
"""
     *
    ***
   *****
  *******
 *********
***********
n=int(input("enter the range "))
for i in range(1 , n+1):
    
    for k in range(1,(n+1)-i):
        print(" ",end="")

    for j in range(0,2*i-1):
        print("*",end = "")
    
    print("")
"""
