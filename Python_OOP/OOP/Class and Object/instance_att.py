class Shop:
    name = 'shoping_mall'

    def __init__(self, owner):
        self.owner = owner
        self.card = []

    def add_to_card(self, item):
        self.card.append(item)


mehjabeen = Shop('mehjabeen')
mehjabeen.add_to_card('mekap')
mehjabeen.add_to_card('phone')
print(mehjabeen.card)
niso = Shop('nisho')
niso.add_to_card('shart')
niso.add_to_card('pant')
print(niso.card)
