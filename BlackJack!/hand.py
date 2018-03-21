class Hand(object):

    def __init__(self):
        self.new_hand()

    # Function that creates a new Hand
    def new_hand(self):
        self.hand = []
        self.total = 0
        self.in_play = True

    # Function that handles the Ace value
    def check_ace(self):
        if(self.in_play):
            for card in self.hand:
                if card.face_value == "A":
                    self.total -= 11
                    self.total += card.ace()

    # Function that checks if a split is possible
    def check_split(self):
        if (self.hand[0].get_face() == self.hand[1].get_face()):
            s = input("Would you like to split your Hand? [Y/N]\n")
            if (s == "Y" or s == "y"):
                return self.split()
            elif (s == "N" or s == "n"):
                return [self]
            else:
                s = input("Invalid Input. Please try again.\n")
        else:
            return [self]

    # Add a card to Hand
    def hit(self, card):
        if(self.in_play):
            self.add_card(card)

    # Function that splits a Hand if possible
    def split(self):
        hands = []
        hand1 = Hand()
        hand1.add_card(self.hand[0])
        hand2 = Hand()
        hand2.add_card(self.hand[1])
        hands.append(hand1)
        hands.append(hand2)
        return hands

    # Function that adds a new Card to the Hand
    def add_card(self, card):
        if(self.in_play):
            self.hand.append(card)
            self.total += card.get_value()
