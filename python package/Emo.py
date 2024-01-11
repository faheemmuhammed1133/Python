from login import *

def ask():
    a = (int(input("""What's your energy level like right now?
1.I'm ready to conquer the world!
2.I am not in for a pancake !!
3.I might just be in for a pancake 
""")))
    if a==1:
        from high import High_Questions
        p=High_Questions()
    elif a==2:
        from low import Low_Questions
        p=Low_Questions()
    elif a==3:
        from Moderate import Moderate_Questions
        p=Moderate_Questions()
    else:
        ask()

main()
print()
ask()