user_input = int(input("Enter your number : "))
factorial = 1
while user_input > 0:
    factorial*= user_input
    user_input-= 1
print(f"The Factorial of your number is {factorial}")