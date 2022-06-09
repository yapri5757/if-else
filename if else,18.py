physics=int(input("enter number"))
chemistry=int(input("enter number"))
biology=int(input("enter number"))
mathametics=int(input("enter number"))
computer=int(input("enter number"))
total=physics+chemistry+biology+mathametics+computer
percentage=total//5
if percentage>=90:
    print("grade A")
elif percentage>=80:
    print("grade B")
elif percentage>=70:
    print("grand C")
elif percentage>=60:
    print("grand D")
elif percentage>=40:
    print("grand E")
else:
    print("fail")

