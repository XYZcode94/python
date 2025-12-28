
from datetime import datetime

# Get current date and time
now = datetime.now()

# print(f"Full Date: {now}")
# print(f"Day of the month: {now.day}")
# print(f"Day name (Short): {now.strftime('%a')}") # e.g., Mon
print(f"Today is {now.strftime('%A')}")  # e.g., Monday

user_age = int(input("Please enter your age : "))
current_day = now.strftime('%A')
if user_age == 100:
    print("AI recommended not watch movies😊")
else:
    if user_age == 0:
        print("enter valid age")

    elif user_age < 5:
        print("you are not ready for movies show")

    elif user_age < 18:
        ticket_price = 12
        if current_day == "wednesday":
            discount = 2
            final_price = ticket_price - discount
            print(f"you ticket price is ${final_price} ")
        else:
            print(f"you ticket price is ${ticket_price} ")
    elif (user_age >= 18 and user_age < 51):
        ticket_price = 18
        if current_day == "wednesday":
            discount = 2
            final_price = ticket_price - discount
            print(f"you ticket price is ${final_price} ")
        else:
            print(f"you ticket price is ${ticket_price} ")

    elif (user_age >= 51 and user_age <= 79):
        print("you take rest😊")

    elif user_age >= 80:
        print("you should not watch movies😊")
    else:
        print("AI recommended not watch movies😊")
