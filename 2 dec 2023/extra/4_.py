# WAP to output how  many sundays did you leave till now
d=int(input("enter your Day of birth "))
m=int(input("enter your Month of birth "))
y=int(input("enter your Year of birth "))
for i in range(2023,y-1,-1):
    if y==i:
        for j in range(12,m-1):
            print(j)
    else:
        for j in range(12,0):
            print(j)