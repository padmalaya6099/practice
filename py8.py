def life(a,b):
    if a>b:
        return a
    else:
        return b
x=int(input("enter first number: "))
y=int(input("enter second number: "))
z=int(input("enter third number: "))
s=int(input("enter forth number: "))
print(life(life(x,y),life(z,s)))
