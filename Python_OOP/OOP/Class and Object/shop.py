class Shop:
    card = []

    def __init__(self, owner):
        self.owner = owner

    def add_to_card(self, item):
        self.card.append(item)


mehjabeen = Shop('mehjabeen')
mehjabeen.add_to_card('mekap')
mehjabeen.add_to_card('shose')
print(mehjabeen.card)

niso = Shop('niso')
niso.add_to_card('T-shart')
niso.add_to_card('watch')
print(niso.card)
