user_input = input("Enter the word : ")
list = []
for i in user_input:
    if user_input.count(i) == 1:
        x = user_input.count(i)
        list.append(f"Character: {i}, Count: {x}")
        print(f"Character: {i}, Count: {x}")

for i in user_input:
    if user_input.count(i) == 2:
        x = user_input.count(i)
        list.append(f"Character: {i}, Count: {x}")
        print(f"Character: {i}, Count: {x}")
        
print(list)
        