import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Convert price and quantity to appropriate types
        price = float(price)
        quantity = int(quantity)
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = item.get('price'),
                quantity = item.get('quantity'),
            )
            

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

class Phone(Item):
    # all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):
        # Call to super function to have acces to all attributes/methods
        super().__init__(
            name, price, quantity
        )
        # Convert price and quantity to appropriate types
        # price = float(price)
        # quantity = int(quantity)
        # broken_phone = int(broken_phone)

        # # Run validations to the received arguments
        # assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        # assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        # assert broken_phone >= 0, f"Broken Phone {broken_phone} is not greater or equal to zero!"

        # Assign to self object
        # self.name = name
        # self.price = price
        # self.quantity = quantity
        # self.broken_phone = broken_phone

        # Actions to execute
        # Phone.all.append(self)


phone_1 = Phone('Xiaomi', 29000, 5, 1)
# print(phone_1.calculate_total_price())
print(Item.all)
print(Phone.all)


# Item.instantiate_from_csv()  
# print(Item.all)


# phone = Item('Iphone', 65000, 5)
# laptop = Item('MacBook', 144000, 3)
# cable = Item('usb type-c', 440, 10)
# mouse = Item('Logitech', 900, 20)
# keybord = Item('Razor', 4999, 2)

# print(Item.all)
# for instance in Item.all:
#     print(instance.name)

# phone.apply_discount()
# print(phone.price)
# laptop.pay_rate = 0.7
# laptop.apply_discount()
# print(laptop.price)

# print(phone.name)
# print(laptop.name)

# print(phone.price)
# print(laptop.price)

# print(phone.quantity)
# print(laptop.quantity)

# print(phone.calculate_total_price())
# print(laptop.calculate_total_price())

# print(Item.pay_rate)
# print(Item.__dict__) # All the attributes for class level
# print(phone.__dict__) # All the attributes for instance level