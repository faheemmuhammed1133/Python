# # WAP to build a parking charge calculaor like upro 3 hours and rate after 3 hrs x ₹/hr 
# vehicles  <=3   >3 per hour rate
# t/b      100       30
# car      70        20
# cycle    50        10
hrs3={"C":10,"B":20,"T":20,"S":5,"BC":5,"M":5}
hrs3Plus={"C":20,"B":30,"T":30,"S":10,"BC":10,"M":10}
vehicle={"C":"Car","B":"Bus","T":"Truck","S":"Scooter","BC":"Bycycle","M":"Motorbike"}
n=input("Enter Your Name ")
x=input("enter the type of vehicle (c for car, s/bc/m for 2 wheeler,t/ b for bus and truck) ").upper()
inTime,intime=(input("enter the time of entry (24 format )")).split(":")
outTime,outtime=(input("enter the time of exit (24 format )")).split(":")
timein=int(inTime)*60+int(intime)
timeout=int(outTime)*60+int(outtime)
if timein > timeout:
    d=24-(timein-timeout)
    t=d=24-(timein-timeout)/60
else:
    d=(timeout-timein)
    t=(timeout-timein)/60
print(t)
extratime=t-3
if t >3:
    fixedcharge=hrs3[x]*3
    charge=fixedcharge+hrs3Plus[x]*extratime
else:
    charge=hrs3[x]*t
print("____________Iparrking______________")
print("Name        :",n,"\n\nVehicle type:__|Duration______Rent______")

print(vehicle[x],"           |",d,"minutes   |",charge)


"""To find the whole number of hours: 
285
60
=
4
60
285
​	
 =4 hours
Remaining minutes: 
285
 minutes
−
(
4
 hours
×
60
 minutes/hour
)
=
45
 minutes
285 minutes−(4 hours×60 minutes/hour)=45 minutes
So, 285 minutes is equivalent to 4 hours and 45 minutes."""