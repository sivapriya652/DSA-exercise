#Ask user for temperature in Celsius.
Celsius=float(input("enter the temperature:"))
Fahrenheit= (Celsius*(9/5))+32
if Celsius<0:
    print("very cold!wear a thick jacket")
elif Celsius>=0 and Celsius<=15:
    print("cold.wear jacket")
elif Celsius>=16 and Celsius<=25:
    print("nice weather")
else:
    print("hot!stay hydrated")
