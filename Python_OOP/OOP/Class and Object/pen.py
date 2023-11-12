# class Calculator:
#     name = "Oppo"

#     def add(self, num1, num2):
#         print(num1+num2)

#     def minus(self, num1, num2):
#         print(num1-num2)

#     def multi(self, num1, num2):
#         print(num1*num2)

#     def divide(self, num1, num2):
#         print(num1/num2)


# my_cal = Calculator()
# my_cal.add(10, 20)
# my_cal.minus(20, 10)
# my_cal.multi(20, 10)
# my_cal.divide(20, 10)


class Pen:
    name = 'matador'

    def __init__(self, ownr, brand, price):
        self.ownr = ownr
        self.brand = brand
        self.price = price

    def sell(self, text):
        print(f'This {text} is a number one brand')


my_pen = Pen('my', 'fresh', 10)
my_pen2 = Pen('her', 'fresh', 10)
print('1', my_pen.ownr, my_pen.brand, my_pen.price)
print('2', my_pen2.ownr, my_pen2.brand, my_pen2.price)
my_pen.sell('matador')
