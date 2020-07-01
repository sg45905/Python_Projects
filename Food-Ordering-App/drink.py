'''
@author - Sarthak Gupta
'''

from menu_item import MenuItem

# define the drinkable menu item class - inherit menu item class
class Drink(MenuItem):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    # define the info method to display details
    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.volume) + 'mL)'
