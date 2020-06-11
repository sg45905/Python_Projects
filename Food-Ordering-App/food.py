from menu_item import MenuItem

# define the eatable menu item class - inherit menu class
class Food(MenuItem):
    def __init__(self, name, price, calorie_count):
        super().__init__(name, price)
        self.calorie_count = calorie_count
    
    # define the info method to display details
    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kcal)'
    
    # define a mrethod to display calorie info
    def calorie_info(self):
        print('kcal: ' + str(self.calorie_count))
