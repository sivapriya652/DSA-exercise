#Ask user for two exam scores (0–100)
subject1=int(input("enter score of subject 1:"))
subject2=int(input("enter score of subect 2:"))
if subject1>=50 and subject2>=50:
    print("you passed!")
else:
    print("you need to retake some exams")
