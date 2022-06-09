age=int(input("enter nummber"))
sex=int(input("enter number"))
day=int(input("enter number"))
if age>=18 and day<30 and sex=="m":
    total=day*700
    print("total",total)
elif age>=18 and day<30 and sex=="f":
    total=day*750
    print("total",total)
elif age>=30 and day<40 and sex=="m":
    total=day*800
    print("total",total)
elif age>=30 and day<40 and sex=="f":
    total=day*850
    print("total",total)