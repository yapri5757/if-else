unit=int(input("enter the number"))
if unit>=100 and unit<200:
    cost=unit*5
    print("total cost=",cost)
elif unit>=200:
    cost=unit*10
    print("total cost=",cost)
else:
    print("no charge")