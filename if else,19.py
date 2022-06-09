basic_salary=float=(input("enter number"))
if basic_salary<=10000:
    HRA=20/100
    DA=80/100
    yr=basic_salary+HRA+DA
    print("gross salary",yr)
elif basic_salary<=20000:
    HRA=25/100
    DA=90/100
    ya=basic_salary+HRA+DA
    print("gross salary",ya)
elif basic_salary>=20000:
    HRA=30/100
    DA=95/100
    yp=basic_salary+HRA+DA
    print("gross salary",yp)
else:
    print("none")

