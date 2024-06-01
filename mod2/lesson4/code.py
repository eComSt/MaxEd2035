numbers = []
for num in range(1, 100001):
    numbers.append(num)

numbers = [num**2 for num in range(1, 11) if num%2 == 0]
print(numbers)
