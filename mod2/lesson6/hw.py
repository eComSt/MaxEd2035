numbers_sum = 0
nonnumeric_lines_count = 0
file = open("data.txt", "r")
lines = file.readlines()
for line in lines:
    try:
        numbers_sum += int(line)
    except ValueError:
        nonnumeric_lines_count += 1
file.close()
print("Сумма чисел:", numbers_sum)
print("Количество будущих шоколадных батончиков:", nonnumeric_lines_count)

