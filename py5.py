n=int(input("enter your first number: "))
p=int(input("enter your last range: "))
for i in range(n,p):
    if i%2==0:
        print(f"{i} is an even number")
    else:
        print(f"{i} is an odd number")
