# wap to unpack a tuple in several variables
'''t=(1,"abc",3)
for i in range(len(t)):
    print(chr(65+i),"=",t[i])
'''
#  wap to remove empty tuple from a list
'''l=[(),(),("",),('a','b'),('a','b','c'),('d')]
r= [x for x in l if x !=() ] # comprehension
# for i in range(5):
#     if l[i]==():
#         l.pop(i)
print(r)
'''
# wap to unzip a list of tuple into individual list
'''l=[(),(),("",),('a','b'),('a','b','c'),('d')]'''
"""for i in range(len(l)):
    print(chr(97+i),"=",list(l[i]))"""
'''i=0
for i in l:
    if(i==l[0]):
        l.pop(l[i])
print(l)'''
# wap to calculate parking charger enter the type of vehicle as character (c for car , b for bus,t for truck) 
# and number of hours ,then calculate charges as given below truck/bus = 20 ph, car = 10 ph ,scooter/ cycle/ motorbike = 5 ph
'''charges={"C":10,"B":20,"T":20,"S":5,"BC":5,"M":5}
x=input("enter the type of vehicle (c for car, s/bc/m for 2 wheeler,t/ b for bus and truck) ").upper()
y=int(input("Enter the hours parked ")) 
print("parking charges for vehicle ",x,"is ₹",charges[x]*y)'''

