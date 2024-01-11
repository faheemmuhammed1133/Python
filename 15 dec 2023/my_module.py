# my module to be imported 
class Addition:
    def add(self,x,y):
        self.x=x
        self.y=y
        print("sum is",self.x+self.y)
class Substraction:
    def sub(self,x,y):
        print("difference is",x-y)
    def diff(self,x,y):
        if x>y:
            print("absolute difference is",x-y)
        else:
            print("absolute difference is",y-x)
class Division:
    def rat(self,x,y):
        if x>y:
            print("div is",x/y)
        else:
            print("div is",y/x)
if __name__=='__main__':
    print("the module name of my_module is",__name__)
    a=Addition()
    a.add(3,7)
    print("executed without importing / directly ")
else:
    print("imported ")


