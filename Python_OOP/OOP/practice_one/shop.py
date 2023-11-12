class Shop:
    def __init__(self, id, name, address,):
        self.id = id
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.address}"


myShop = Shop(1, 'My shop', "dhaka")
print(myShop)
