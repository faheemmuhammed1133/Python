n=int(input("enter the range "))
for i in range(1 , n+1):
    for k in range(n+1-i,1,-1):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end = "")
    for k in range(2*(n+1-i),1,-1):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end = "")
    
    print("")