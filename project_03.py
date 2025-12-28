from datetime import datetime
now = datetime.now()

print(f"Today is {now.strftime('%A')}")
user_marks = int(input("Enter your test marks : "))
if user_marks > 100:
    print("Enter valid marks \n Marks should be upto 100")
else:
    if (user_marks == 100 or user_marks >= 90):
        print(F"you have scored A grade.")
    elif (user_marks == 90 or user_marks > 80):
        print(F"you have scored B grade.")
    elif (user_marks == 80 or user_marks > 70):
        print(F"you have scored C grade.")
    elif (user_marks == 70 or user_marks > 60):
        print(F"you have scored D grade.")
    elif (user_marks == 60 or user_marks > 50):
        print(F"you have scored E grade.")
    else:
        print(F"you failed in test.")
