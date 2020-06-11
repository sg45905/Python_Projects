# calculate total fare
class HotelFareCal:
    def __init__(self, room_total='', room_rent=0, game_bill=0, food_cost=0, laundry_bill=0, service_charge=1800, name='', address='', cin_date='', cout_date='', room_no=101):
        self.room_total = room_total
        self.food_cost = food_cost
        self.laundry_bill = laundry_bill
        self.game_bill = game_bill
        self.room_rent = room_rent
        self.service_charge = service_charge

        self.name = name
        self.address = address
        self.cin_date = cin_date
        self.cout_date = cout_date
        self.room_no = room_no
    
    # function for taking data
    def inputData(self):
        self.name = input("\n Enter your name                          : ")
        self.address = input("\n Enter your address                       : ")
        self.cin_date = input("\n Enter your check in date (dd-mm-yyyy)    : ")
        self.cout_date = input("\n Enter your check out date (dd-mm-yyyy)   : ")

        print("Your room no. : " + str(self.room_no) + "\n")
        
    # calculate the room rent
    def roomRent(self):
        print("\n ----- Welcome to Highway Retreat ----- \n")

        print("We have the following types of rooms for you : \n")
        
        print("1. Type - A : Rs.6000 / Night")
        print("2. Type - B : Rs.5000 / Night")
        print("3. Type - C : Rs.4000 / Night")
        print("4. Type - D : Rs.3000 / Night")

        room_ch = int(input("\n Enter your room choice please : "))
        print("\n")
        nights = (int(self.cout_date[0:2]) - int(self.cin_date[0:2]))

        if room_ch == 1:
            print("You have opted for Type - A")
            self.room_rent = 6000 * nights
        elif room_ch == 2:
            print("You have opted for Type - B")
            self.room_rent = 5000 * nights
        elif room_ch == 3:
            print("You have opted for Type - C")
            self.room_rent = 4000 * nights
        elif room_ch == 4:
            print("You have opted for Type - D")
            self.room_rent = 3000 * nights
        else:
            print("Atleast choose a room to proceed...")

        print("\n Your Room Rent is = " + str(self.room_rent) + "\n")

    # calculate restaurant bill
    def restaurantBill(self):
        print("\n ----- Welcome to the Highway Retreat Restaurant Service ----- \n")

        print("1. Water              : Rs.20")
        print("2. Tea                : Rs.10")
        print("3. Breakfast combo    : Rs.90")
        print("4. Lunch combo        : Rs.110")
        print("5. Dinner combo       : Rs.150")
        print("6. Exit")

        while (1):
            menu_ch = int(input("\n Enter your menu choice please : "))

            if menu_ch == 1:
                qty = int(input("Enter the quantity : "))
                print("\n")
                self.food_cost += 20*qty
            elif menu_ch == 2:
                qty = int(input("Enter the quantity : "))
                print("\n")
                self.food_cost += 10*qty
            elif menu_ch == 3:
                qty = int(input("Enter the quantity : "))
                print("\n")
                self.food_cost += 90*qty
            elif menu_ch == 4:
                qty = int(input("Enter the quantity : "))
                print("\n")
                self.food_cost += 110*qty
            elif menu_ch == 5:
                qty = int(input("Enter the quantity : "))
                print("\n")
                self.food_cost += 150*qty
            elif menu_ch == 6:
                break
            else:
                print("\n Please choose correct menu item...")

        print("\n Total Restaurant Bill = Rs." + str(self.food_cost) + "\n")

    # calculate laundry bill
    def	laundryBill(self):
        print("\n ----- Welcome to the Highway Retreat Laundry Service ----- \n")

        print("1. Shorts    : Rs.3")
        print("2. Trousers  : Rs.4")
        print("3. Shirt     : Rs.5")
        print("4. Jeans     : Rs.6")
        print("5. Girlsuit  : Rs.8")
        print("6. Exit")

        while (1):
            laundry_ch = int(input("\n Enter your laundry choice : "))

            if laundry_ch == 1:
                qty = int(input("Enter the quantity : "))
                print("\n")
                self.laundry_bill += 3*qty
            elif laundry_ch == 2:
                qty = int(input("Enter the quantity : "))
                print("\n")
                self.laundry_bill += 4*qty
            elif laundry_ch == 3:
                qty = int(input("Enter the quantity : "))
                print("\n")
                self.laundry_bill += 5*qty
            elif laundry_ch == 4:
                qty = int(input("Enter the quantity : "))
                print("\n")
                self.laundry_bill += 6*qty
            elif laundry_ch == 5:
                qty = int(input("Enter the quantity : "))
                print("\n")
                self.laundry_bill += 8*qty
            elif laundry_ch == 6:
                break
            else:
                print("\n Please select a valid option...")

        print("\n Total Laundary Bill = Rs." + str(self.laundry_bill) + "\n")

    # calculate gaming bill
    def gameBill(self):
        print("\n ----- Welcome to the Highway Retreat Gaming Parlour ----- \n")

        print("1. Table tennis  : Rs.60 / hr")
        print("2. Bowling       : Rs.80 / hr")
        print("3. Snooker       : Rs.70 / hr")
        print("4. Video games   : Rs.90 / hr")
        print("5. Pool          : Rs.50 / 6-shots / hr")
        print("6. Exit")

        while (1):
            game_ch = int(input("\n Enter your gaming choice : "))

            if game_ch == 1:
                hrs = int(input("No. of hours : "))
                print("\n")
                self.game_bill += 60*hrs
            elif game_ch == 2:
                hrs = int(input("No. of hours : "))
                print("\n")
                self.game_bill += 80*hrs
            elif game_ch == 3:
                hrs = int(input("No. of hours : "))
                print("\n")
                self.game_bill += 70*hrs
            elif game_ch == 4:
                hrs = int(input("No. of hours : "))
                print("\n")
                self.game_bill += 90*hrs
            elif game_ch == 5:
                hrs = int(input("No. of hours : "))
                print("\n")
                self.game_bill += 50*hrs
            elif game_ch == 6:
                break
            else:
                print("\n Please choose a valid option")

        print("\n Total Gaming Bill = Rs." + str(self.game_bill) + "\n")

    # display all details
    def display(self):
        self.roomRent()
        self.restaurantBill()
        self.laundryBill()
        self.gameBill()

        print ("\n ----- Highway Retreat Billing System ----- \n")

        print ("Customer name       : " + self.name)
        print ("Customer address    : " + self.address)
        print ("Check in date       : " + self.cin_date)
        print ("Check out date      : " + self.cout_date)
        print ("Room no.            : " + str(self.room_no))
        print ("Room Rent           : " + str(self.room_rent))
        print ("Restaurant Bill     : " + str(self.food_cost))
        print ("Laundary Bill       : " + str(self.laundry_bill))
        print ("Gaming Bill         : " + str(self.game_bill))

        self.room_total = self.room_rent + self.food_cost + self.laundry_bill + self.game_bill

        print ("Sub-total           : " + str(self.room_total))
        print ("Service Charges     : " + str(self.service_charge))
        print ("Total               : " + str(self.room_total + self.service_charge) + "\n")
        
        self.room_no += 1
