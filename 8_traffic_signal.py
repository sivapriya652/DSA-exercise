#Create a simple traffic light simulator
#the signal must be red ,yellow or green
signal=input("the red or yellow or green signal:")
if signal=="red" or signal=="Red" or signal=="RED":
    print("stop!")
elif signal=="yellow" or signal=="Yellow" or signal=="YELLOW":
    print("prepare to stop")
elif signal=="green" or signal=="Green" or signal=="GREEN":
     print("you can go")
else:
    print("wrong input!")
