#function vs method
class ATM:
    pin = ''
    balance = 0
    def __init__(self):
#         __init__ method is nothing but a constructor of that class
        choice="0"
        while(choice!="5"):
            self.showMenu()
            choice=input()
            if choice=='1':
                self.setPin()
            elif choice=='2':
                self.deposit()
            elif choice=='3':
                self.withdraw()
            elif choice=='4':
                self.showBalance()
    def __str__(self):
        return "Instance of ATM class"

    def showMenu(self):
        print('''
            1)set pin
            2)Deposit
            3)withdraw
            4)Balance
            5)Exit
            
        ''')
    def setPin(self):
        pin=input("Enter Pin")
        self.pin=pin
        print("Pin set Successfully")

    def deposit(self):
        temp_pin=input("Enter Pin")
        if self.pin==temp_pin:
            bal=int(input("enter amount"))
            self.balance=self.balance+bal
        else:
            print("Incorrect pin")
    def withdraw(self):
        temp_pin=input("Enter Pin")
        if self.pin==temp_pin:
            bal=int(input("enter amount"))
            if bal<self.balance:
                self.balance=self.balance-bal
            else:
                print("Low balance")
        else:
            print("Incorrect pin")

    def showBalance(self):
        print("Your Balance is {}".format(self.balance))
sbi=ATM()






