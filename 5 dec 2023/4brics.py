
brics=["BRAZIL","RUSSIA","INDIA","CHINA","SOUTH AFRICA"]


l=input("enter a country name to check wheather its inn brics or not \n").upper()
for i in range(5):
    k="Not found"
    if brics[i]==l:
        print(l,"is a member in Brics")
        k="found"
        break
if k!= "found":
    print(l,"is not a member in Brics")
       
        
        