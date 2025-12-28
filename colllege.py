number = int(input("Enter a positive integer: "))
composite_factors = []

for i in range(2, number + 1):
    if number % i == 0:
        for j in range(2, int(i**0.5) + 1): 
            if i % j == 0:
                composite_factors.append(i)
                break
        else:
           continue 

print(f"The composite factors of {number} are: {composite_factors}")