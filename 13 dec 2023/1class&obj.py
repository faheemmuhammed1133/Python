#  creating class in python and constructor
"""class Student:
    count=0
    def __init__(self,name,age) :# def __init__(self,name,age) : parameter,def __init__(self) : default constructor
        self.name=name
        self.age=age
        Student.count+=1
    def display(self):
        print("name: ",self.name,"\nage: ",self.age)
obj=Student("abc",19)
obj.display()
obj1=Student("xyz",32)
obj1.display()
print("number of obj =",Student.count)"""

# class practice
'''class Itm:
   countb=0
   countp=0
   def get(self):
    n=int(input("number of entries: "))
    for n in range(n):
        self.name=input("enter name")
        self.age=int(input("enter age"))
        self.dob=input("enter dob")
        self.department=input("enter department(BTECH,PGDM)").upper()
        if self.department=="BTECH":
            Itm.countb+=1
        elif self.department=="PGDM":
            Itm.countp+=1
        else:
            self.name="na"
            self.age="na"
            self.dob="na"
   print("")
   def dis(self):
       for n in range(Itm.countb+Itm.countp):
           print("")
           print("name:",self.name)                                                          
           print("age:",self.age)
           print("dob:",self.dob)
           print("debpartment:",self.department)
           
       print()
       print("number of students in pgdm entered",Itm.countp)
       print("number of students in pgdm entered",Itm.countb)

obj=Itm()
obj.get()
obj.dis()
'''

class Itm:                                  
    countb=0                                    
    countp=0                                    
    def get(self,name,age,dob,department):          
        self.name=name                          
        self.age=age                            
        self.dob=dob
        self.department=department              
        if self.department=="BTECH":            
            Itm.countb+=1                       
        elif self.department=="PGDM":           
            Itm.countp+=1                       
        else:                                   
            self.name=None                      
            self.age=None                       
            self.dob=None                       
            self.department=None                
    def dis(self):                              
        print()                                 
        print("name:",self.name)                
        print("age:",self.age)                  
        print("dob:",self.dob)                  
        print("debpartment:",self.department)
    def __del__(self):
        print("del is called")   
                                                
obj=list()                                      
n=int(input("number of entries: "))             
for i in range(n):                              
    obj.append(Itm())                           
for i in range(n):                                                           
    name=input("enter name") 
    age=input("enter age")   
    dob=input("enter dob")  
    department=input("enter department(BTECH,PGDM)").upper()
    obj[i].get(name,age,dob,department)                                 
for i in range(n):                                              
    obj[i].dis()                                                  
print()                                                            
                                                                      