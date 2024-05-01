songs = {
    'Bad Guy': 3,
    'Thunder': 3,
    'Sweater Weather': 4,
    'Numb': 3,
    'Karma Police': 4,
    'Enjoy the Silence': 4,
    'Obstacles': 3,
    'Crosses': 2,
    'Unnamed Feeling': 7
}
# num  =int(input("Сколько песен выбрать? "))
# summ = 0
# for i in range(num):
#     song = input(f"Название {i+1} песни: ")
#     summ += songs[song]
# print("Общее время звучания песен:",summ,"минут")

# summ = 0 # Вначале устанавливаю сумму равной нулю [5]
# for i in range(int(input("Сколько песен выбрать? "))):
#      summ += songs[input(f"Название {i+1} песни: ")] 
# print("Общее время звучания песен:",summ,"минут")

print(f"Общее время звучания песен:{sum([songs[input(f"Название {i+1} песни: ")] for i in range(int(input("Сколько песен выбрать? ")))])} минут")