class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        balance = 0
        
        for transaction in self.ledger:
            balance += transaction['amount']

        return balance

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination.name}')
            destination.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f'{self.name:*^30}\n'

        output = ""

        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"
            output += f'{description:<23}{amount:>7}\n'

        total = f'Total: {self.get_balance():.2f}'

        return title + output + total

def create_spend_chart(categories):
    withdrawals = []

    for category in categories:
        total = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                total += abs(transaction['amount'])
        withdrawals.append(total)

    total_spent = sum(withdrawals)

    percentages = []
    if total_spent > 0:
        for amount in withdrawals:
            percentage = int((amount / total_spent) * 100)
            percentage = (percentage // 10) * 10
            percentages.append(percentage)
    else:
        percentages = [0] * len(categories)

    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        chart += f'{level:3}| '
        for p in percentages:
            chart += 'o  ' if p >= level else '   '
        if level > 0:
            chart += '\n'
        else:
            chart += '\n'

    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    names = [c.name for c in categories]
    for i in range(max(len(n) for n in names)):
        chart += '     '
        for name in names:
            chart += (name[i] + '  ') if i < len(name) else '   '
        if i < max(len(n) for n in names) - 1:
            chart += '\n'

    return chart

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
