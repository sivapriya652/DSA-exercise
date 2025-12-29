#Ask user for two numbers (as strings), convert them to integer
a=input("enter first number:")
b=input("enter second number:")
x=int(a)
y=int(b)
print("their sum is:",x+y)
print("their difference is:",x-y)
print("their product is:",x*y)
if x>y:
    print(x,"is bigger")
elif x==y:
    print("both are equal")
else:
    print(y,"is bigger")
