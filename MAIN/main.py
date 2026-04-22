# 2
class OnlineShop:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        jami = self.price * self.quantity
        print("Jami:", jami, "so'm")

    def apply_discount(self, percent):
        jami = self.price * self.quantity
        chegirma = jami * percent / 100
        yangi_narx = jami - chegirma
        print("Chegirmadan keyin:", int(yangi_narx), "so'm")



shop = OnlineShop("Daftar", 10000, 3)

shop.total_price()
shop.apply_discount(10)
