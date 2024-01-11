# program to check prime numbers in a given range
a=int(input("enter starting num "))
b=int(input("enter end num "))
x=[]
if a<0:
    a=2
    if b>0:
        for i in range(a,b+1):
            k=0
            for j in range(a,i):
                if i%j==0:
                    k+=1
            if k==0:
                x.append(i)
        print(x)
    else:
        print("INVALID RANGE FOR PRIME NUMBERS")
else:
    if b>0:
        for i in range(a,b+1):
            k=0
            for j in range(2,i):
                if i%j==0:
                    k+=1
            if k==0:
                x.append(i)
        print(x)
    else:
        print("INVALID RANGE FOR PRIME NUMBERS")    
