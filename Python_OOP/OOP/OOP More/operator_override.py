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


sakib = Criceter('sakib', 36, 5.8, 75, 'BD')
sakib.eat()
sakib.exparience()
