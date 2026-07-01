class Bank:
    def __init__(self):
        self.__balance=500
    def deposit(self, amount):
        self.__balance+=amount
    def withdraw(self, amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient Balance")
    
    def show_balance(self):
        print("balance: ", self.__balance)

b=Bank()
b.deposit(1000)
b.withdraw(200)
b.show_balance()