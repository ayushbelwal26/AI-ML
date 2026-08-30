class Product:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"The price of {self.name} is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"The count of object is {cls.count}")

    @staticmethod
    def calc_disc(price,discount):
        final_price = price - (discount*price/100)
        print(f"The final price after discount is {final_price}")


p1 = Product("phone",10_000)
p2 = Product("laptop",40_000)
p3 = Product("pen",10)

p1.get_info()
p2.get_info()
p3.get_info()

Product.get_count()
p1.calc_disc(p1.price,5)
p1.calc_disc(p2.price,10)
p1.calc_disc(p3.price,0)

