# SINGLE INHERITANCE

'''class Parent:
    def add(self):
        return self.x+self.y
class Child(Parent):
    def takeValue(self):
        a=float(input("enter num 1 "))
        b=float(input("enter num 2 "))
        self.x=a
        self.y=b
        return self.add()
obj=Child()
print(obj.takeValue())'''

# area 

'''class Parent:
    def areA(self):
        self.area=0.5*self.x*self.y
        return self.area
class Child(Parent):
    def takeValue(self):
        a=float(input("enter num 1 "))
        b=float(input("enter num 2 "))
        self.x=a
        self.y=b
        # print("area of triangle is",self.areA(a,b))
obj=Child()
obj.takeValue()
print("area of triangle is",obj.areA())'''

#c.add(c.x,c.y)

'''class Parent:
    def areA(self,x,y):#):,
        self.area=0.5*self.x*self.y
        print("area of triangle is",self.area)
class Child(Parent):
    def takeValue(self):
        self.x=float(input("enter num 1 "))
        self.y=float(input("enter num 2 "))
c=Child()
c.takeValue()
c.areA(c.x,c.y)'''

# if ractange or else square

'''class Area:
    l=[]
    def areaSq(self):
        print("area of square is ",self.l[0]*4)
    def areaRec(self):
        print("area of Rectangle is ",self.l[0]*self.l[1])
    def areaTri(self):
        self.s=(self.l[0]+self.l[1]+self.l[2])/2
        self.tArea=(self.s*(self.s-self.l[0])*(self.s-self.l[1])*(self.s-self.l[2]))**0.5
        print("area of Triangle is ",self.tArea)
               
class Inputvalue(Area):
    def takevalue(self):
        j=0
        k=1
        while j<=2 and k !=0:
            k=float(input("enter length/breadth (0 to exit enter 3 sides for triangle) "))
            if k!=0:
                self.l.append(k)
            j+=1
        if len(self.l)==3:
            self.areaTri()
        elif len(self.l)==2:
            self.areaRec()
        elif len(self.l)==1:
            self.areaSq()
        else:
            print("invalid entry! ")
o=Inputvalue()
o.takevalue()'''

# MULTIPLE INHERITANCE

'''class Lu:
    def __init__(self):
       self._sub =["Python","Java","C++"]
       self._professor=["Saikiran Sondarkar","Prasad Sawant","Viral Patel"]
       self._dur=[1.0,2.0,3.0]

class Itm:
    def __init__(self):
       self._subi =["Mba","Business","Abc"]
       self._professori=["Sheetal Ahir","Sumit Shinde","Afroz Khan"]
       self._duri=[1.0,2.0,3.0]

class Btech(Lu,Itm):
    def __init__(self):
        Lu.__init__(self)
        Itm.__init__(self)
    def sub_prof_dur(self):
        self.subj=self._sub+self._subi
        self.prof=self._professor+self._professori
        self.durr=self._dur+self._duri
        print(self.subj,"\n",self.durr) # ,self.prof,"\n"
    def choice(self):
        self.subj = (input("enter the subjects u need ,( separate using \",\")")).split(",")
        totaldur=  0
        print("___________________________________________________\n|SUB\t       | TRAINER\t\t| DURATION|\n___________________________________________________")
        
        for i in self.subj:

            ind=None
            if i in self._sub:
                ind = self._sub.index(i)
                print("|" , i ,((8-len(i))*" "),"   |   " , self._professor[ind], ((18-len(self._professor[ind]))*" "), " | ",self._dur[ind],"hr" , "|")
                totaldur += self._dur[ind]
            else:
                ind = self._subi.index(i)
                print("|" , i ,((8-len(i))*" "),"   |   " , self._professori[ind] ,((17-len(self._professori[ind]))*" "), " | ",self._duri[ind],"hr", "|")
                totaldur += self._duri[ind]
        print("___________________________________________________")
        print("\n\nTotal Duration : ",totaldur)


b=Btech()
b.sub_prof_dur()
b.choice()'''

# romil panday jeeeeeeeeee
'''class Lu:
    def __init__(self):
        self._sub = ["Python","Java","C++"]
        self._trainer = ["Sai Sondarkar Sir","Sumit Sir","Sheetal Ma'am"]
        self._duration = [1.0,2.0,1.5]

class ITM:
    def __init__(self):
        self._sub1 = ["Business" ,"MBA" ,"Pgdm" ]
        self._trainer1 = ["Business Mam" , "MBA Sir" , "Pgdm Mam"]
        self._duration1 = [1.0,2.0,3.0]


class Child(ITM,Lu):

    def __init__(self):
        Lu.__init__(self)
        ITM.__init__(self)
    
    def setsub(self):
        print("\n\nHey Which one of the course you want ? ","LU : ",self._sub,"ITM : ",self._sub1,sep="\n")
        self.subj = (input()).split(",")
    
    def getsub(self):
        totalhour=  0
        print("___________________________________________________\n|SUB\t       | TRAINER\t\t| DURATION|\n___________________________________________________")
        

        for i in self.subj:
            
            index = None
            if(i in self._sub ):
                index = self._sub.index(i)
                print("|" , i ,((8-len(i))*" "),"   |   " , self._trainer[index], ((17-len(self._trainer[index]))*" "), " | ",self._duration[index],"hr" , "|")
                totalhour += self._duration[index]
            else:
                index = self._sub1.index(i)
                print("|" , i ,((8-len(i))*" "),"   |   " , self._trainer1[index] ,((17-len(self._trainer1[index]))*" "), " | ",self._duration1[index],"hr", "|")
                totalhour += self._duration1[index]
        print("___________________________________________________")
        print("\n\nTotal Duration : ",totalhour)



a = Child()
a.setsub()
a.getsub()'''

# MULTILEVEL INHERITANCE

'''class GP:
    def __init__(self):
        # super().__ini
        self.namegp="ABC"
        self.inheritedgp=9999999
        self.purchased="20 BITCOIN "
class P(GP):
    def __init__(self):
        super().__init__()
        self.name="DEF"+" "+self.namegp
        self.inherited=self.inheritedgp
        self.purchased="30 BITCOIN "+self.purchased
class C(P):
    def __init__(self):
        super().__init__()
        self.name="GHI"+" "+self.name
        self.inherited=self.inherited
        self.purchased="10 BITCOIN "+self.purchased
    def myprop(self):
        print()
        print("Hi,",self.name)
        print("inherited assets ",self.inherited)
        print("Purchased assets of whole family ",self.purchased)
        print()
c=C()
c.myprop()'''

# HYBRID INHERITANCE

'''class GP:
    def __init__(self):
        # super().__ini
        self.namegp="ABC"
        self.inheritedgp=9999999
        self.purchased=20
class P(GP):
    def __init__(self):
        super().__init__()
        self.name="DEF"+" "+self.namegp
        self.inherited=self.inheritedgp
        self.purchased=30+self.purchased
class H:
    def __init__(self):
        self.name1="JKL MNO PQR"
        self.inherited1=1111111
        self.purchased1=73
class C(P,H):
    def __init__(self):
        super().__init__()
        H.__init__(self)
        self.name="GHI"+" "+self.name+" "+self.name1
        self.inherited=self.inherited+self.inherited1
        self.purchased=10+self.purchased+self.purchased1
    def myprop(self):
        print()
        print("Hi,",self.name)
        print("inherited assets ",self.inherited)
        print("Purchased assets of whole family ",self.purchased,"BITCOIN")
        print()
c=C()
c.myprop()'''

# library check out check in system

class Library:
    def fcb(self):
        part={1:"Books",2:"Dvd",3:"Journal"}
        print("what do you want to choose \n",part)
        self.choice=int(input())
        if self.choice==1:
            self.b=Books()

        elif self.choice==1:
            d=Dvd()
            
        else:
            self.j=Journal()
    def checkOut(self):
        print()
        
class Journal(Library):
    def __init__(self):
        self.record=["1.abc","2.def","3.ghi","4.jkl","5.mno","6.pqr","7.stu","8.vwx","9.yx"]
        self.livestock=[0,20,10,33,12,16,18,32,24,7]
        print(self.record)
        self.option=int(input("enter the seriel no of the book you want (enter 0 for check out)"))
        if self.option !=0:
            if self.livestock[self.option]!=0:
                print("you have succesfully isuued",self.record[self.option-1])
                self.k=self.livestock[self.option]-1
                self.livestock[self.option]=self.k
                print(self.livestock[self.option]-1)
        else:
            l.checkOut("Journal")
class Books(Library):
    def __init__(self):
        self.record=["1.abc","2.def","3.ghi","4.jkl","5.mno","6.pqr","7.stu","8.vwx","9.yx"]
        self.livestock=[0,20,10,33,12,16,18,32,24,7]
        print(self.record)
        self.option=int(input("enter the seriel no of the book you want (enter 0 for check out)"))
        if self.option !=0:
            print("you have succesfully isuued",self.record[self.option-1])
            self.k=self.livestock[self.option]-1
            self.livestock[self.option]=self.k
            print(self.livestock[self.option])
        else:
            l.checkOut("Books")
class Dvd(Library):
    def __init__(self):
        self.record=["1.abc","2.def","3.ghi","4.jkl","5.mno","6.pqr","7.stu","8.vwx","9.yx"]
        self.livestock=[0,20,10,33,12,16,18,32,24,7]
        print(self.record)
        self.option=int(input("enter the seriel no of the book you want (enter 0 for check out)"))
        if self.option !=0:
            print("you have succesfully isuued",self.record[self.option-1])
            self.k=self.livestock[self.option]-1
            self.livestock[self.option]=self.k
            print(self.livestock[self.option])
        else:
            l.checkOut("Dvd")
l=Library()
l.fcb()

