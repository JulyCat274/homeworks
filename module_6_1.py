class Animal:

    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        self.food = Plant

        if food.edible is False:
            print(self.name, 'не стал есть', food.name)
        else:
            print(self.name, 'съел', food.name)

        if food.edible is True:
            self.alive = True
        else:
            self.alive = False

        if food.edible is True:
            self.fed = True
        else:
            self.fed = False

class Plant:

    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):

    def __init__(self, name):
        super().__init__(name)
        self.edible = True
        self.name = name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
