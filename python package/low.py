
from bookmoviedata import Low
# low energy switch

# low   \
point=0
class Low_Questions: 
    
    def __init__(self):

        def q1():

            global point
            x=int(input("""How is your patience ?
1.good
2.bad 
Your Input: """))
            if x==1:
                point+=10
            elif x==2 :
                point+=0
            else:
                print("""INVALID ENTRY!
Only Enter Intigers(1,2)
Try Again!""")
                q1()

        def q2():

            global point
            x=int(input("""Are you a problem solver ? 
1.yes
2.no
Your Input:  """))
            if x==1:
                point+=10
            elif x==2 :
                point+=0
            else:
                print("""INVALID ENTRY!
Only Enter Intigers(1,2)
Try Again!""")
                q2()

        def q3():

            global point
            x=int(input("""How good is your literature ? 
1.good
2.bad
Your Input:  """))
            if x==1:
                point+=20
            elif x==2 :
                point+=10
            else:
                print("""INVALID ENTRY!
Only Enter Intigers(1,2)
Try Again!""")
                q3()

        def switchcase():

            # global point
            if point/40 ==1:
                
                x=Low()
                x.novels()
                x.classicmovies()
                exit()
            elif point/40==0.5:
                x=Low()
                x.mysterybooks()
                x.mysterymovies()
                exit()
            elif point/40==0.25:
                x=Low()
                x.fictionbooks()
                x.indiemovies()
                exit()
            else:
                # print("Switch  To Moderate")
                from Moderate import Moderate_Questions
                p=Moderate_Questions()


        q1()
        q2()
        q3()
        switchcase()

    # low()
l=Low_Questions()

        