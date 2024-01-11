# functions trials
'''def func(name,age):
    print("Name :",name)
    print("Age  :",age)
func(name="Abc",age="32")
func(age="34",name="Abc")
func("Abc",32)
# func(32,name="abc")  error
# func(age=32,"abc")   error'''

'''c=90
def main():
    a=10
    b=4
    global c # if its active (in function main..........dir() = ['a', 'b'])  else:(in function main..........dir() = ['a', 'b', 'c'])
    c=4+b
    
    # printing the scope of variables
    print("in function main..........dir() =",dir())
    result=absdiff(a,b)
    # printing absolute difference
    print("The absolute difference of",a,"-",b,"=",result)
def absdiff(x,y):
    # printing the scope of variables
    print("in function absdiff..........dir() =",dir())
    if x>y:
        z=x-y
    else:
        z=y-x
    return z
main()'''

# destance between two points
'''def distance(x1,x2,y1,y2):
    # s=1/2
    print((((x1-x2)**2)+((y1-y2)**2))**0.5)
    # print(dis)

distance(1,4,2,6)'''

# composition
'''def area():
    r=distance(1,2,4,6)
    print("in area   ...",dir())
    print("Area is",(22/7)*(r**2))

def distance(x,y,h,k):
    print("in distance   ...",dir())
    return((((x-h)*(x-h))+((y-k)*(y-k))) #**0.5)
    # for i in range(100):
    #     for j in range(100):
    #         if j == ((x-h)*(x-h))+((y-k)*(y-k))**0.5:
    #             print("*",end="")
    #     print()
    # return r**0.5

    
area()'''

'''# for i in range(2*r+1):
    '''
#  factorial ÷
def fact(n):
    if n==0:
        return 1
    else:
        r=n*fact(n-1)
        return r
try:
    n=int(input("enter a number to find factorial "))
    print(fact(n))
except:
    print("invalid input")