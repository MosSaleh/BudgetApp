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
    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
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
        if self.check_funds(amount) == False:
            return False
        else:
            withdraw_description = "Transfer to " + othercategory.name
            self.withdraw(amount, withdraw_description)

            deposit_description = "Transfer from " + self.name
            othercategory.deposit(amount, deposit_description)
            return True

    def check_funds(self, amount):
        # function that checks how much money is in category (used in other functions to test if statements can be executed)
        balance = self.get_balance()
        new_balance = balance - amount
        if new_balance < 0:
            return False
        else:
            return True

    def title_maker(self):
        # function which makes the title of the output
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


def create_spend_chart(categories):
    # function which creates a bar graph of percentage of spending for each category based on the withdrawals
    total_withdraw = 0
    category_dict = dict()
    for category in categories:

        ledger = category.ledger
        category_withdraw = 0
        for item in ledger:
            if item["amount"] < 0:
                category_withdraw += item["amount"] * -1
            else:
                pass
        category_dict[category.name] = category_withdraw

    for category, withdraw in category_dict.items():
        total_withdraw += withdraw

    cat_percent = dict()

    for category, withdraw in category_dict.items():
        perc = (withdraw / total_withdraw) * 100
        if perc < 10:
            perc = 0
            fin_perc = int(1)
        else:
            first_num = str(perc)[0]
            fin_perc = int(first_num) * 10

        cat_percent[category] = fin_perc

    leftpercentage = 100
    string = ""
    for i in range(11):
        if leftpercentage == 0:
            string += " "
        if leftpercentage != 100:
            string += " " + str(leftpercentage) + "| "
        else:
            string += str(leftpercentage) + "| "

        for category, percentage in cat_percent.items():
            if percentage >= leftpercentage:
                string += "o  "
            else:
                string += "   "

        string += "\n"
        leftpercentage -= 10

    barchart_numbers = string

    def horizontal_line():
        # function which creates the horizontal dashes for the bar chart
        cat_number = len(cat_percent)
        hor_line = "    " + "----"
        for i in range(cat_number - 1):
            hor_line += "---"
        return hor_line

    def words():
        # function which returns the names of the categories in a vertical fashion under the barchart

        category_list = []
        for category, percentage in cat_percent.items():
            category_list.append(category)

        longest_word = ""

        for cat in category_list:
            if len(cat) > len(longest_word):
                longest_word = cat
        word_output = ""
        for i in range(len(longest_word)):

            word_output += "\n"
            word_output += "     "

            for cat in category_list:

                if cat == category_list[0]:
                    try:
                        if cat[i] == cat[0]:
                            word_output += str(cat[i]).capitalize() + "  "
                        else:
                            word_output += str(cat[i]) + "  "
                    except:
                        word_output += " " + "  "

                else:

                    try:
                        if cat[i] == cat[0]:
                            word_output += str(cat[i]).capitalize() + "  "
                        else:
                            word_output += str(cat[i]) + "  "
                    except:
                        word_output += " " + "  "

        return word_output

    word_output = words()
    hor_line = horizontal_line()
    title = "Percentage spent by category\n"

    output = title + barchart_numbers + hor_line + word_output
    return output
