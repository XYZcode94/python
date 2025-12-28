user_input = int(input("Enter the number which you want to write table : "))
skip_line = int(input("Enter the number which you want to skip in  table : "))

print(f"table of {user_input}\n")
for i in range(1, 11):
    if i == skip_line:
        continue
    print(f"{user_input} X {i} = {user_input * i}")

    