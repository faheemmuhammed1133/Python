# testing my module
'''import my_module as mm # assigning alice name
from importlib import reload
reload(mm) # to reflect changes done in my_module  (jupiter me kam padega)

a=mm.Addition()                     # a=my_module.Addition()  
x=int(input("enter a num 1 "))
y=int(input("enter num 2 "))
a.add(x,y)
s=mm.Substraction()
s.diff(x,y)
s.sub(x,y)
d=mm.Division()
d.rat(x,y)'''

# avoiding division and only including from my_module
# from my_module import Addition,Substraction   # to import Addition and Substraction only from my_module
'''x=int(input("enter a num 1 "))
y=int(input("enter num 2 "))
a=Addition()
a.add(x,y)
s=Substraction()
s.diff(x,y)'''

# '__main__'
import my_module as mm
x=int(input("enter a num 1 "))
y=int(input("enter num 2 "))
a=mm.Addition()
a.add(x,y)
s=mm.Substraction()
s.diff(x,y)