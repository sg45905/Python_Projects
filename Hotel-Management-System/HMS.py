# main program
from Hotel import HotelFareCal

import sys

# object of the HotelFareCal class
bill = HotelFareCal()

while(1):
    print("\n ----- Welcome to Highway Retreat Billing System ----- \n")

    print("1. Enter customer details ...")
    print("2. Calculate room rent ...")
    print("3. Calculate restaurant bill ...")
    print("4. Calculate laundry bill ...")
    print("5. Calculate gaming bill ...")
    print("6. Display complete bill ...")
    print("7. EXIT")

    bill_ch = int(input("\n Enter your choice for the menu above : "))
    print("\n")
    
    if bill_ch == 1:
        bill.inputData()
    elif bill_ch == 2:
        bill.roomRent()
    elif bill_ch == 3:
        bill.restaurentBill()
    elif bill_ch == 4:
        bill.laundryBill()
    elif bill_ch == 5:
        bill.gameBill()
    elif bill_ch == 6:
        bill.display()
    elif bill_ch == 7:
        sys.exit(0)
