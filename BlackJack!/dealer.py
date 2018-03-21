from hand import Hand
from money import Money


class Dealer(object):

    # Initializer
    def __init__(self):
        self.money = Money()
        self.hand = Hand()

    # Handles betting from the dealer's end
    def bet(self, bet_amt):
        if(self.money.bet_amt >= bet_amt):
            self.money.bet_amt = bet_amt
            self.money.remove(bet_amt)
        else:
            self.money = Money()
            self.money.bet_amt -= bet_amt

    # Handles gameplay from dealer's end. WILL ADD MORE HERE
    def play(self, game):
        while (self.hand.total < 17):
            self.hand.add_card(game.deck.draw_card())

    # Prints dealer's hand total for player info
    def dealer_status(self):
        print("Dealer's hand total was : %d \n" % self.hand.total)
