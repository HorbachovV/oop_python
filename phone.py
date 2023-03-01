from item import Item

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