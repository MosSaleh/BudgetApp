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
    def withdraw(self, amount, description =''):
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

    def title_maker(self):
        x = ""
        firstpart_len = int((30 - len(self.name)) / 2)
        for i in range(firstpart_len):
            x += "*"
        x += self.name
        remaining_len = 30 - firstpart_len - len(self.name)
        for i in range(remaining_len):
            x += "*"
        title = x
        return title

    def line_maker(self):
        lines = ""

        for item in self.ledger:

            description = item["description"]
            amount = item["amount"]
            amount = "{0:.2f}".format(amount)[:7]
            # amount = float(amount)
            # amount = round(amount, 2)
            description = description[:23]

            description_len = len(description)
            amount_len = len(str(amount))

            space_len = 30 - description_len - amount_len
            lines += description
            for i in range(space_len):
                lines += " "
            lines += str(amount)
            lines += "\n"
        balance = self.get_balance()
        balance = "{0:.2f}".format(balance)
        lines += "Total: " + str(balance)

        return lines

    def __str__(self):
        title = self.title_maker()
        lines = self.line_maker()
        print_output = title + "\n" + lines
        return print_output

#food = Category("food")
#
#
#food.deposit(2500)
## print(food.get_balance())
#(food.withdraw(21, "pizza"))
#print(food.withdraw(2000, "sushi"))
## print(food.withdraw(2050, "cookies"))
#print(food)
#clothes = Category("clothes")
#
#(food.transfer(200, clothes))
## print(clothes.ledger)
#print(clothes.ledger)


def create_spend_chart(categories):
