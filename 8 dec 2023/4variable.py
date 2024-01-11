# variable scope
'''glob=4
def func():
    # global glob # u can acces the value of global varible value inside the function , to change u have to add global keyword
    glob=3
    print(glob)
func()
print(glob)'''

var1=10 # global
def fun():
    var1=3 # nonlocal
    print(var1)
    def fun2():
        # nonlocal var1
        # global var1
        var1=4
        print(var1)
    fun2()
    print(var1)
fun()
print(var1)