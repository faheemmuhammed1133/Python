from random import randint  # from random import * will import all functions in random module

class Atm:
    name=""
    card="123456789876"
    __pin=card[11:7:-1]
    __balance=float(randint(99,1000000))
    def __init__(self):
        print("Hello")
        print("please insert your card ")
        self.c=randint(99999999999,1000000000000)
        self.card=str(self.c)
        self.__pin=int(self.card[11:7:-1])
        print("enter you name as in card ",self.card)
        self.n=input()
        self.name= self.n
        
    def withdrawal(self):
        print(self.name,"How much money do you want to withdraw")
        self.w=float(input())
        self.p=int(input("enter your pin ")) 
        if self.p==self.__pin:
            if self.w >self.__balance:
                print("Out of Balnce")
            else:
                print(self.w,"Withdrwan succesfully")
                self.__balance-=self.w
                print("remaining Balnce is ₹",self.__balance)
        else:
            print("Wrong Pin !")
            # break
    def deposite(self):
        print("hey",self.name,"enter the amount to deposite ")
        self.w=float(input())

        self.p=int(input("enter your pin "))
        if self.p==self.__pin:
            print("",self.w,"deposited succesfully")
            self.__balance+=self.w
            print("Updated Balnce is ₹",self.__balance)
        else:
            print("Wrong Pin !")
            # break
    def balncecheck(self):
        print("hey",self.name,"enter your pin ")
        self.p=int(input()) 
        if self.p==self.__pin:
            print(f"{self.name} Your ACCOUNT XXXXXXXX{self.card[8:12]}\nRemaining Balace is ₹{self.__balance}") #f string ignore spaces in variable 
        else:
            print("Wrong Pin !")
            # break
            


