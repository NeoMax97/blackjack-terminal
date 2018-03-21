class Money(object):

    # Function that sets up initial values
    def __init__(self):
        self.balance = 100
        self.bet_amt = 0

    # Function that receives input from player about bet amount
    def bet(self):
        amt = int(input("Please place your bet between $5 and $100:\n"))
        while (amt < 5 or amt > 100):
            amt = int(input("Invalid amount. Please try again:\n"))
        self.bet_amt = amt
        self.remove(amt)
        return amt

    # Function that removes money from balance
    def remove(self, amount):
        self.balance -= amount
        return amount

    # Function that adds money to balance
    def add(self, amount):
        self.balance += amount
