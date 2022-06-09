a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a>b and a<c:
    print("a is second largest")
elif b>a and b<c:
    print("b is second largest")
elif c>a and c<b:
    print("c is second largest")
else:
    print("none is second largest")