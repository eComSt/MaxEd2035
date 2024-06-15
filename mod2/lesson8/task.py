class Hero:
    def __init__(self, name, hp, damage, armor):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def get_status(self):
        print(f"{self.name} has {self.hp} health, {self.damage} damage, and {self.armor} armor.")
        print('-'*50)

    def increase_armor(self):
        if self.armor*1.5 < 100:
            self.armor = self.armor*1.5
            print(f"Armor increased to {self.armor}.")
        else:
            print("Armor is already at max.")
        print('-'*50)

    def decrease_armor(self):
        if self.armor > 0:
            self.armor -= 10
        else:
            print("Armor is already at min.")

    def give_damage(self, enemy):
        print(f'Атака по персонажу {enemy.name}!')
        print('-'*50)
        enemy.get_damage(self.damage)

    def get_damage(self, damage):
        absorbed_damage = damage * self.armor/100
        finally_damage = damage - absorbed_damage
        self.hp -= finally_damage
        print(f'По герою {self.name} нанесли урон {finally_damage}!')
        print('-'*50)
hero = Hero("Batman", 100, 10, 10)
hero2 = Hero("Spiderman", 50, 20, 50)
hero.increase_armor()
hero2.give_damage(hero)
hero.get_status()
