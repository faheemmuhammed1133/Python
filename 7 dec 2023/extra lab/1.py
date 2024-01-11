# wap to add a tuple to a list
'''a=[1,3,5,6]
b=(67,46,78)
a+=list(b)
print(a)'''
# size of a tuple
'''a=(966,77,88,"car","roy",87.65)
print(len(a))'''

# wap to create a list of a tuples from given list having numbers and its cube in each tuple
a=[2,3,4,5,6]
lt=[0,0,0,0,0]
j=[]
for i in range(len(a)):
        j+=(a[i],a[i]**3)
        lt[i]=tuple(j[i*2:i*2+2])
print(lt)
    
    