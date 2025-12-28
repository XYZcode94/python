user_input = input("Enter your word to reverse : ")
reverse_str = ""
for i in user_input:
    reverse_str = i + reverse_str
print(reverse_str)