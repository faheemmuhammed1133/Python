"""
star j==1+4*i or
"""


# star j==1+4*i or

# x=int(input("enter the rows "))

for i in range(1,6):
    for n in range(14):
        print(" ",end="")
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(2*i+2):
        if k==0 or k==2*i+1 :
            print("$",end="")
        else:
            print(" ",end="") 
    print(" ")
    for n in range(14):
        print(" ",end="")
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(2*i):
        # if k==2*i-1 :
            print(" ",end="")
        # else:
            print(" ",end="") 
    print(" ")

for i in range(1):
    for j in range(11):
       print("$  ",end=" ")
    print("")
for i in range(6):
    for j in range(1,39):
        if j==13-i or j==24+i :
            # or j==6*i+1 or j==40-6*i-2
            print(" $",end=" ")
            # print(" ",end="")
        else:
            print(" ",end="")
    print(" ")    
    for j in range(1,39):
        if j==6*i+1 or j==40-6*i-3:
            print(" $",end="")
            # print(" ",end="")
        else:
            print(" ",end="")
    print(" ")
# x=int(input("enter the rows "))

'''for i in range(1,5+1):
    for n in range(14):
        print(" ",end="")
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2 :
            print("$",end="")
        else:
            print(" ",end="") 
    print(" ")
    for n in range(14):
        print(" ",end="")
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(2*i):
        if k==2*i-1 :
            print(" ",end="")
        else:
            print(" ",end="") 
    print(" ")

for i in range(1):
    for j in range(14):
       print("$",end="  ")
    print("")
for i in range(6):
    for j in range(1,39):
        if j==13-i or j==24+i :
            # or j==6*i+1 or j==40-6*i-2
            print("$",end=" ")
            # print(" ",end="")
        else:
            print(" ",end="")
    print(" ")    
    for j in range(1,39):
        if j==6*i+1 or j==40-6*i-3:
            print("$",end="")
            # print(" ",end="")
        else:
            print(" ",end="")
    print(" ")'''