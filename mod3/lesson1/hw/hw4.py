class Dog:
    def __init__(self, name, happy=0):
        self.__name = name
        self.__happiness = happy
    def caress(self):
        self.__happiness+= 10
        print("Gav-Gav")
    def get_name(self):
        print(f"Dog's name: {self.__name}")
    def set_name(self, name):
        self.__name = name
        print(f"Dog's name now: {self.__name}")
    def bring_item(self, item, d):
        if d<=100 and self.__happiness>=10:
            print(f"Dog {self.__name} brought {item} to the garden")
        else:
            if d>100:
                print("Dog is too tired to bring the item")
            if self.__happiness<10:
                print("Dog is not happy enough to bring the item")

Lucky = Dog("Lucky")
Lucky.caress()
Lucky.get_name()
Lucky.bring_item("ball", 100)
Lucky.set_name("Lucky")