class Calculator:
    name = "cico"

    def add(self, num1, num2):
        return num1+num2

    def minus(self, num1, num2):
        return num1-num2

    def multiplay(self, num1, num2):
        return num1*num2

    def divide(self, num1, num2):
        return num1 / num2


my_cal = Calculator()
my = my_cal.add(10, 20)
print(my)
my1 = my_cal.minus(20, 10)
print(my1)
my2 = my_cal.multiplay(5, 4)
print(my2)
my3 = my_cal.divide(30, 5)
print(my3)
