class Wallet:
    def __init__(self, currency, balance):
        self.currency = currency
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount

    def spend_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Not enough balance!")

    def show_balance(self):
        print("Balance: ", self.balance, self.currency)

error = 0
currency = input("Enter currency: ")
if currency != "USD" and currency != "BGN" and currency != "EUR":
    print("Invalid currency!")
    error = 1

if error != 1:
    balance = float(input("Enter initial balance: "))
    user = Wallet(currency, balance)

    opt = 0
    while opt != 6:
        print("\n1. Add money")
        print("2. Spend money")
        print("3. Show balance")
        if user.currency == "USD":
            print("4. USD -> BGN")
            print("5. USD -> EUR")
        elif user.currency == "EUR":
            print("4. EUR -> BGN")
            print("5. EUR -> USD")
        elif user.currency == "BGN":
            print("4. BGN -> USD")
            print("5. BGN -> EUR")
        print("6. Exit")

        opt = int(input("Enter option (1-6): "))

        if opt == 1:
            amount = float(input("Enter amount to add: "))
            user.add_money(amount)
        elif opt == 2:
            amount = float(input("Enter amount to spend: "))
            user.spend_money(amount)
        elif opt == 3:
            user.show_balance()
        elif opt == 4:
            if user.currency == "USD":
                user.balance *= 1.6
                user.currency = "BGN"
            elif user.currency == "EUR":
                user.balance *= 1.96
                user.currency = "BGN"
            elif user.currency == "BGN":
                user.balance /= 1.6
                user.currency = "USD"
        elif opt == 5:
                if user.currency == "USD":
                    user.balance /= 1.2
                    user.currency = "EUR"
                elif user.currency == "EUR":
                    user.balance *= 1.2
                    user.currency = "USD"
                elif user.currency == "BGN":
                    user.balance /= 1.96
                    user.currency = "EUR"
        elif opt == 6:
            print("Exited...")
        else:
            print("Invalid option")