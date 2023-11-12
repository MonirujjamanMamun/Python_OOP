class Products:
    def __init__(self, name, price, quntity, color) -> None:
        self.name = name
        self.price = price
        self.quntity = quntity
        self.color = color
        self.allProduct = []


class Shop(Products):
    def __init__(self, id, shopName, address, name, price, quntity, color, allProduct) -> None:
        super().__init__(name, price, quntity, color, allProduct)
        self.id = id
        self.shopName = shopName
        self.address = address

    def __str__(self) -> str:
        return f"Id= {self.id}, ShopName= {self.shopName}, address = {self.address}, product name= {self.name}, prodict price= {self.price}, product quntity= {self.quntity}, product color = {self.color}."

    def add_product(self, Products):
        # product = {'name': self.name, 'price': self.price,
        #            'quntity': self.quntity, 'color': self.color}
        product = Products
        self.allProduct.append(product)

    def buy_products(self):
        userProduct = input('Provide Product Name: ')
        for product in self.allProduct:
            if userProduct == product:
                self.allProduct.pop('product')
                return f'Congress Sucessfully you buy {product} products'
            else:
                return f"{userProduct} Isn't availabel now."


myShop = Shop()
myShop.add_product('')
print(myShop)
