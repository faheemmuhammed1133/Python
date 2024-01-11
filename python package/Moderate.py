#Moderate.
from bookmoviedata import Moderate

mark=0
class Moderate_Questions():
    def __init__(self):
        def mq1():
            global mark
            a=int(input("""Do you like Black or White ?
1.Black
2.White
Your Input: """))
            if a==1:
                mark+=20
            elif a==2:
                mark+=0
            else:
                print("Invalid Input")
                mq1()
        def mq2():
            global mark
            b=int(input("""Interested in Past or Future ?
1.Past
2.Future
Your Input: """))
            if b==1:
                mark+=10
            elif b==2:
                mark+=10
            else:
                print("Invalid Input")
                mq2()
        def mq3():
            global mark
            c=int(input("""What is your age group ?
1.0-30
2.30+
Your Input: """))
            if c !=1 and c!=2:
                print("Invalid Input")
                mq3()
            if (mark)/30==1:
                from low import Low_Questions
                a=Low_Questions()


            elif (mark)/30==0.33:
                # print("HIGH CALL")
                from high import High_Questions
                x=High_Questions()
            else:
                if c ==1:
                    x=Moderate()
                    x.scifibooks()
                    x.scifimovies()
                    exit()
                    
                elif c == 2:
                    x=Moderate()
                    x.historybooks()
                    x.historymovies()
                    exit()

        mq1()
        mq2()
        mq3()
# if __name__=='__main__':
m=Moderate_Questions()