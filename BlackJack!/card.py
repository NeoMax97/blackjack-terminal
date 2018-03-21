class Card(object):

    # Initializer Function
    def __init__(self):
        self.suit = ""
        self.face_value = ""
        self.int_value = 0

    # Function that return a card object
    def new_card(self, suit, value):
        self.suit = suit
        self.face_value = value

        if (value == "A"):
            self.int_value = 11
        elif (value == "J" or value == "Q" or value == "K"):
            self.int_value = 10
        else:
            self.int_value = int(value)
        return self

    # Function that checks the value of Ace in hand
    def ace(self):
        val = int(input("Would you like to use your Ace as 1 or 11?\n"))
        while (val != 1 and val != 11 and Card.face_value == "A"):
            val = int(input("Invalid input. Please try again:\n"))
        self.face_value = " A "
        self.int_value = val
        return val

    # Function that returns suit of card as string
    def get_suit(self):
        return self.suit

    # Function that returns face value as string
    def get_face(self):
        return self.face_value

    # Function that returns value of card as int
    def get_value(self):
        return self.int_value
