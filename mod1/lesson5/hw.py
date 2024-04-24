numbers = input().split()
sum_numbers = 0

for num in numbers:
    sum_numbers += int(num)

average = sum_numbers / len(numbers)
print(average)