"""
    ✺ 
   ✺ ✺ 
  ✺   ✺ 
 ✺     ✺ 
✺       ✺ 
 ✺     ✺ 
  ✺   ✺ 
   ✺ ✺ 
    ✺
"""
x=int(input("enter the rows"))
for i in range(1,x+1):
    for j in range(x,i,-1):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print("✺",end="")
        else:
            print(" ",end="") 
    print(" ")
for i in range(x-1,0,-1):
    for j in range(x,i,-1):
        print(" ",end="")
    for k in range(2*i-1):
        if  k==0 or k==2*i-2:
            print("✺",end="")
        else:
            print(" ",end="")    
    print(" ")    