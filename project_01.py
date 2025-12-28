user_input = input("Enter your age : ")
age = int(user_input)
if age == 0:
    print("enter valid age")
elif  age < 18:
    print("you are teenager")
elif age < 28:
    print("you are youth of india ")
elif age <51:
    print("your are is the back bone of family")
elif age < 60:
    left_age = 60- (age)
    print(f"your are just gone retire in {left_age} year")
else:
    print("you take rest😊")