from datetime import datetime
now = datetime.now()
print(f"Today is {now.strftime('%A')}")
print("1. Banana\n2. Apple\n3. Mango ")
User_input = int(input("Choose one fruit from above : "))
match User_input:
    case 1:
        fruit = "Banana"
        print("1. Yellow\n2. Brown\n3. Green")
        User_input = int(input("Choose colour of Banana : "))
        match User_input:
            case 1:
                print(f"Good quality {fruit}")
            case 2:
                print(f"Bad quality {fruit}")
            case 3:
                print(f"Unripe {fruit}")
            case _:
                print("invalid input")
    case 2:
        fruit = "Apple"
        print("1. Red\n2. Light red\n3. Green")
        User_input = int(input("Choose colour of Banana : "))
        match User_input:
            case 1:
                print(f"Good quality {fruit}")
            case 2:
                print(f"Bad quality {fruit}")
            case 3:
                print(f"Unripe {fruit}")
            case _:
                print("invalid input")
    case 3:
        fruit = "Mango"
        print("1. Yellow\n2. light yellow\n3. Green\n4. light green")
        User_input = int(input("Choose colour of Banana : "))
        match User_input:
            case 1:
                print(f"Good quality {fruit}")
            case 2:
                print(f"Bad quality {fruit}")
            case 3:
                print(f"Unripe {fruit}")
            case 4:
                print(f"wait for some day to ripe {fruit}")
            case _:
                print("invalid input")
    case _:
        print("invalid input")
               
                
