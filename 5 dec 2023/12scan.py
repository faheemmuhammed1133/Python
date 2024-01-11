# WAP that scans an email addres and for a tuple of username and domain
usernameT=()
domainT=()
domains=['isu.ac.in',"itm.edu","gmail.com","outlook.com","hotmail.com"]
nat=0
d="a"
for j in range(5):
    x=input("enter email addres ")
    for i in range(len(x)):
        if x[i]=="@":
            nat=i
            d=x[nat+1:]
    for i in range(5):
        if d==domains[i]:
            domainT=x[nat+1:]
            print(domainT)
        else:
            print("domain not found ")
            break
    usernameT=x[:nat]

    print('Username=',usernameT)
    print("domain=",domainT)

    print("in work")