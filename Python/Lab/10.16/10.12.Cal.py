x=float(input("x="))
y=float(input("y="))
z=input("z=")
if z == "sum":
    print(x+y)
elif z == "sub":
    print(x-y)
elif z == "multiplication":
    print(x*y)
elif z == "divide":
    if y == 0:
        print("cannot divide by 0")
    else:
        print(x/y)
