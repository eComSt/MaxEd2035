from random import randint

class Human:
    def __init__(self, name, health):
        self._name = name
        self._health = health
    def attack(self, enemy):
        dmg = randint(1, 10)
        enemy.get_damage(dmg)
        print(f"{self._name} наносит персонажу {enemy._name} {dmg} урона!.")
    def get_damage(self, dmg):
        self._health -= dmg
        print(f"{self._name} получает {dmg} урона! Текущее здоровье — {self._health}.")
    def healing(self):
        heal = randint(5, 15)
        self._health += heal
        print(f"{self._name} восстанавливает {heal} здоровья! Текущее здоровье — {self._health}.")

class Warrior(Human):
    def __init__(self, name, health, defense):
        super().__init__(name, health)
        self._defense = defense
    def attack(self, enemy):
        dmg = randint(10, 20)
        enemy.get_damage(dmg)
        print(f"{self._name} наносит персонажу {enemy._name} {dmg} урона!.")
    def get_damage(self, dmg):
        if dmg > self._defense: dmg-=self._defense
        else: dmg = 0
        super().get_damage(dmg)

class Archer(Human):
    def __init__(self, name, health, accuracy, agility):
        super().__init__(name, health)
        self._accuracy = accuracy
        self._agility = agility
    def attack(self, enemy):
        dmg = randint(15, 25)*self._accuracy
        enemy.get_damage(dmg)
        print(f"{self._name} наносит персонажу {enemy._name} {dmg} урона!.")
    def get_damage(self, dmg):
        if randint(1, 100) > self._agility:
            super().get_damage(dmg)
        else:
            print(f"{self._name} увернулся от удара!")

human = Human("Вася", 80)
warrior = Warrior("Волк", 120, 5)
archer = Archer("Лошадь", 90, 1.15, 10)
human.attack(warrior)
warrior.attack(archer)
archer.healing()