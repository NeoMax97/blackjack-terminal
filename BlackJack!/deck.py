# import numpy as np
from card import Card
import random


# Class to handle decks
class Deck(object):

    # Initializer
    def __init__(self):
        self.values = {"A", "2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "J", "Q", "K"}
        self.suits = {"♠", "♣", "♦", "♥"}
        self.deck = []
        self.new_deck()

    # Function that sets up a new deck
    def new_deck(self):
        for suit in self.suits:
            for value in self.values:
                card = Card()
                self.deck.append(card.new_card(suit, value))
                # self.deck.append(suit + " " + value)
        # self.np_deck = np.array(self.deck)

        # return self.np_deck
        return self.deck

    # Function to draw a card from the Deck
    def draw_card(self):
        self.reshuffle_deck()
        index = random.randint(0, (len(self.deck) - 1))
        card = self.deck[index]
        self.remove_card(card)
        return card

    # Reshuffles Deck when almost over to keep the game going
    def reshuffle_deck(self):
        if(len(self.deck) < 10):
            print("Deck is almost over. Reshuffling Deck.\n")
            self.__init__()

    # Function to remove a card from the Deck
    def remove_card(self, card):
        self.deck.remove(card)
        # CHECK IF THE LINE ABOVE IS RIGHT
