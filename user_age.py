#Ask user for their age
age=int(input("enter your age:"))
if age<13:
    print("you are a child")
elif age>=13 and age<=17 :
    print("you are a teenager")
elif age>=18 and age<=64:
    print("you are an adult")
elif age>=65:
    print("you are a senior")
