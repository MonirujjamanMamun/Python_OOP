class Shopping:
    name = 'My-Shop'

    def __init__(self, name):
        self.name = name
        self.card = []

    def add_to_card(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.card.append(product)

    def check_out(self, amount):
        total = 0
        for item in self.card:
            total += item['price']*item['quantity']

        print(f'total amount', total)
        if total < amount:
            print(f'Your extra amount is {amount-total}')
        else:
            print(f'You need {total-amount} more')


ml_shopon = Shopping('ML-Shopon')
ml_shopon.add_to_card('alue', 50, 5)
ml_shopon.add_to_card('potol', 30, 3)
ml_shopon.add_to_card('dim', 15, 2)

print(ml_shopon.card)
ml_shopon.check_out(200)
