print("module name of first ",__name__)
def add(x,y):
    print(x+y)

if __name__=='__main__':

    add(6,9)
else:
    print("printing imported ",__name__)