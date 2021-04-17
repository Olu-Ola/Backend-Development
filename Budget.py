class Budget:
    def __init__(self, name):
        self.name = name
        self.store = []

    def withdraw(self, amount):
        if self.check_available_amount(amount):
            self.store.append({"amount": -amount})
            return True
        else:
            return False

    def deposit(self, amount,):
        self.store.append({"amount": amount})

    def get_balance(self):
        total = 0
        for item in self.store:
            total += item['amount']
        return total

    def transfer(self, amount, budget_category):
        if self.check_available_amount(amount):
            self.withdraw(amount)
            budget_category.deposit(amount)
            return True
        else:
            return False

    def check_available_amount(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False


food = Budget('Food')
Clothing = Budget('Clothing')
food.deposit(1000)
print(food.get_balance())  # This will print out 1000
food.transfer(600, Clothing)
print(food.get_balance())  # This will print 400
print(Clothing.get_balance())  # This  will print 600
