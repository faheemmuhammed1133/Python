from bookmoviedata import High
mark=0
class High_Questions():
    def __init__(self):
        def hq1():
            global mark 
            a=int(input("""Do you have a Love Life? 
1.YES
2.NO
"""))
            if a==1:
                mark+=0
            elif a==2:
                mark+=10
            else:
                print("Invalid Input")
                hq1()
        def hq2(): 
            global mark 
            b=int(input("""Are You Creative ?
1.Yes
2.No
"""))
            if b==1:
                mark+=10
            elif b==2:
                mark+=0
            else:
                print("Invalid Input")
                hq2()
        def hq3(): 
            global mark 
            c = int(input("""Scale Your Humour
1.(0-3)
2.(4-7)
3.(8-10)"""))
            if c==1:
                mark+=10
            elif c==2:
                mark+=10
            elif c == 3:
                mark+=0
            else:
                print("Invalid Input")
                hq3()


            if (mark)/30==1:
                print("FANTASY")
                x=High()
                x.fantasybooks()
                x.fantasymovies()
                exit()
            elif (mark)/30==0.33:
                print("ROMANCE")
                x=High()
                x.romanticbooks()
                x.romanticmovies()
                exit()
            elif (mark)/30==0:
                print("COMEDY")
                x=High()
                x.comedybooks()
                x.comedymovies()
                exit()

            else :
                d = int(input("""Do You Lucid Dream ?
1.Yes
2.No
"""))
                if d == 1:
                    # print("LOW")
                    from low import Low_Questions
                    a=Low_Questions()
                elif d == 2 :
                    print("COMEDY")
                    x=High()
                    x.comedybooks()
                    x.comedymovies()
                    exit()
        hq1()
        hq2()
        hq3()
h=High_Questions()