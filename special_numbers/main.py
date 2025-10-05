numbers = [5, 12, 18, 21, 33, 42, 50, 77, 90]
special_numbers = []

for i in range(9):
    if numbers[i] > 20:
        if numbers[i] % 3 == 0:
            if numbers[i] % 5 != 0:
                special_numbers.append(numbers[i])

print(special_numbers)