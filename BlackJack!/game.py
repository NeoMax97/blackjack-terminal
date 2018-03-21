from deck import Deck
from display import Display
from hand import Hand
from money import Money
from command import Command
from dealer import Dealer


class Game(object):

    '''
    turn = 0
    game_over = False
    money = 0
    deck = 0
    hand = 0
    hands = []
    input = 0
    '''
    # Initializer for Game object
    def __init__(self):
        self.turn = 0
        self.game_over = False
        self.deck = Deck()
        self.hand = Hand()
        self.hands = []
        self.hands.append(self.hand)
        self.money = Money()
        self.command = Command()
        self.dealer = Dealer()

    def play(self):
        self.money.bet()
        self.dealer.bet(self.money.bet_amt)
        self.dealer.play(self)
        for hand in self.hands:
            hand.add_card(self.deck.draw_card())
        self.turn += 1
        cmd = 1
        while(self.hand.total < 21 and cmd == 1 and not self.game_over):
            print("Turn number : %d" % self.turn)
            # Adds and draws the cards of every hand
            for hand in self.hands:
                hand.add_card(self.deck.draw_card())
                Display.draw_cards(hand)
                Display.hand_total(hand)
            # Displays important information
            Display.view_info(self.money.balance, self.money.bet_amt)
            # Checks if hand needs handling of Ace
            for hand in self.hands:
                hand.check_ace()
            # Checks if player can split
            if (self.turn == 1):
                self.hands = self.hand.check_split()
            self.turn += 1
            # Checks if round is over
            for hand in self.hands:
                self.game_over = self.over(hand)
                if (self.game_over):
                    self.hands.remove(hand)
                    break
            # Gets input for action on each Hand
            for hand in self.hands:
                cmd = self.command.action(hand, self)
        # Asks player for another round
        # Display.view_info(self.money.balance, self.money.bet_amt)
        self.dealer.dealer_status()
        self.play_again()

    # Function that resets values for a new round
    def reset(self):
        self.turn = 0
        self.hand = Hand()
        self.hands = []
        self.hands.append(self.hand)
        self.game_over = False
        self.dealer = Dealer()

    # Function that asks player for another round
    def play_again(self):
        again = input("Would you like to play again? [Y/N]\n")
        if(again == "Y" or again == "y"):
            self.reset()
            self.play()
        elif(again == "N" or again == "n"):
            print("Thanks for playing!")
        else:
            again = input("Invalid option. Please try again")

    # Function that checks if game is over
    def over(self, hand):
        if(hand.in_play):
            if hand.total == 21:
                hand.in_play = False
                print("! ! ! BLACKJACK ! ! !\n")
                self.money.balance += self.money.bet_amt
                return True
            elif hand.total > 21:
                hand.in_play = False
                print("X X X BUST X X X\n")
                return True
            else:
                return False
