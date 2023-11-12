class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print(f'eat rice')

    def exparience(self):
        raise EnvironmentError


class Criceter(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):
        print(f'Eat vagitables')

    def exparience(self):
        print('He is an exparience player.')

    def __add__(self, other):
        return self.age + other.age

    def __mul__(self, other):
        return self.age * other.age

    def __len__(self):
        return self.name


sakib = Criceter('sakib', 36, 5.8, 75, 'BD')
sakib.eat()
sakib.exparience()
mushi = Criceter('mushi', 36, 5.3, 70, 'BD')
print(mushi.age + sakib.age)
print(mushi.age * sakib.age)
print(len(mushi.name))
