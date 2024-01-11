# wap that has a class store which keep the record of item code and price display a menu of all products to the user and
# prompt him the quantity of each item required finally generate a bil  and total amount (item priceand code in private) 
import random
class Store:
    def products(self,name,code,price):
        self.productName=name
        self.__productCode=code
        self.__productPrice=price
    def dis(self,i):
        
        print(i+1,"|  ",self.productName,"    |   ",self.__productPrice,"    |   ",self.__productCode)
    def cart(self,i):
        cartlist=[]

obj=list()                                      
'''n=int(input("number of entries: "))             
for i in range(n):                              
    obj.append(Store())                           
for i in range(n):                                                           
    name=input("enter name") 
    code=random.randint
    price=int(input("enter price") )
    obj[i].get(name,code,price)'''
for i in range(4):
    obj.append(Store())

obj[ 0 ].products("Product A","A001",    10)
obj[ 1 ].products("Product B","A002",    17)
obj[ 2 ].products("Product C","A003",    20)
obj[ 3 ].products("Product D","A004",    12)
'''obj[ 4 ].products("Product E","A005",    18)
obj[ 5 ].products("Product F","A006",    25)
obj[ 6 ].products("Product G","A007",    30)
obj[ 7 ].products("Product H","A008",    22)
obj[ 8 ].products("Product I","A009",    28)
obj[ 9 ].products("Product J","A0010",   16)
obj[ 10 ].products("Product K","A0011",  19)
obj[ 11 ].products("Product L","A0012",  21)
obj[ 12 ].products("Product M","A0013",  14)
obj[ 13 ].products("Product N","A0014",  17)
obj[ 14 ].products("Product O","A0015",  23)
obj[ 15 ].products("Product P","A0016",  27)
obj[ 16 ].products("Product Q","A0017",  29)
obj[ 17 ].products("Product R","A0018",  26)
obj[ 18 ].products("Product S","A0019",  31)
obj[ 19 ].products("Product T","A0020",  24)'''
print("__All Products__  , price     ,  productID")                              
for i in range(4):                                              
    obj[i].dis(i)                                                  
print("_________________________________________")
j=0
cart=[]

while j!=0:
    j=int(input("enter the seriel number product you want to buy (enter 0 to exit)"))
    if j!=0:
        obj.cart()