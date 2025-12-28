user_input = int(input("Enter the values where to calculate even sum of numbers : "))
even_sum = 0
for num in range(0, user_input+1):
    if num % 2 == 0:
        # print(num)
        even_sum+= num
print(even_sum)
