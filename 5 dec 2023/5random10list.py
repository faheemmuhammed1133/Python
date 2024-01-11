# to create random 10 numbers into list
import random
l=[]
strt=int("enter start of from where to where you want the random 10 numbers")
end=int("enter start off rom where to where you want the random 10 numbers")
for i in range(10):
    
    l.append(random.randint(strt,end))
print(l)