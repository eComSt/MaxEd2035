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

summ = 0 # Вначале устанавливаю сумму равной нулю [5]
for i in range(int(input("Сколько песен выбрать? "))): summ += songs[input(f"Название {i+1} песни: ") ] 
print("Общее время звучания песен:",summ,"минут")