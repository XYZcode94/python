from datetime import datetime
now = datetime.now()
print(f"Today is {now.strftime('%A')}")
print("1. sunny\n2. rainy\n3. snowy")
User_input = int(input("Choose weather condition : "))
match User_input:
    case 1:
      print("go for walk")
    case 2:
      print("take an umbrella")
    case 3:
      print("take rest in room")      
    case _:
      print("invalid input")