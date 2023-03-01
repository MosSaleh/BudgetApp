class Category:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.ledger = []

    # deposits amount while adding a description to the ledger list
    # if no description then defaults to empty string
    def deposit(self, amount, description=""):

        self.ledger.append({"amount": amount, "description": description})

    # withdraws amount and also adds description to ledger list
    def withdraw(self, amount, description):
        if self.checkfunds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    # shows balance of category
    def get_balance(self):
        balance = self.balance
        for i in self.ledger:
            balance += i["amount"]
        return balance

    def transfer(self, amount, othercategory):
        if self.checkfunds == False:
            return False
        else:
            withdraw_description = "Transfer to " + othercategory.name
            self.withdraw(amount, withdraw_description)

            deposit_description = "Transfer from " + self.name
            othercategory.deposit(amount, deposit_description)
            return True

    def checkfunds(self, amount):
        balance = self.get_balance()
        new_balance = balance - amount
        if new_balance < 0:
            return False
        else:
            return True


food = Category("food")

food.deposit(2500)
# print(food.get_balance())
(food.withdraw(20, "pizza"))
print(food.withdraw(2000, "sushi"))
# print(food.withdraw(2050, "cookies"))

clothes = Category("clothes")

(food.transfer(200, clothes))
# print(clothes.ledger)
print(clothes.ledger)


# def create_spend_chart(categories):
