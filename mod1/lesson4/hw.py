numbers = []
squares = []

for _ in range(5):
    number = int(input())
    numbers.append(number)
    squares.append(number ** 2)

squares.sort(reverse=True)
print(squares)