# define the menu item class
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # define the info method to display details
    def info(self):
        return self.name + ': $' + str(self.price)

    # define the total price method to calculate total price of the order
    def get_total_price(self, count):
        total_price = self.price * count

        # if bulk order - provide discount
        if count >= 3:
            total_price *= 0.9

        return round(total_price)
