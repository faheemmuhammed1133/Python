# WAP to check grade
x=float(input("Hello student. How many mark did you score"))
if x<=50:
    print("you are failed")
elif x<=60:
    print("Passed")
elif x<=70:
    print("Average")
elif x<=80:
    print("Good")
elif x<=90:
    print("Great")
else:
    print("Topper")
