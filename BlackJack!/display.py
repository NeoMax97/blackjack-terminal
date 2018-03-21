# Class to handle important 'GUI' elements
class Display(object):

    # Draw cards in hand on terminal
    def draw_cards(hand):
        if hand.in_play is True:
            for i in range(len(hand.hand)):
                print(" _ _ _ _ _    ", end="")
            print("\n")

            for card in hand.hand:
                suit = card.get_suit()
                value = card.get_face()
                print("|%s        |   " % value, end="")
            print("\n")

            for card in hand.hand:
                suit = card.get_suit()
                value = card.get_face()
                print("|    %s    |   " % suit, end="")
            print("\n")

            for card in hand.hand:
                suit = card.get_suit()
                value = card.get_face()
                print("|        %s|   " % value, end="")
            print("\n")

            for i in range(len(hand.hand)):
                print(" - - - - -    ", end="")
            print("\n")

    # Function for showing important info to the player
    def view_info(money, bet_amt):
        print("Money Left : %d | Bet Amount : %d \n" % (money, bet_amt))

    # Function to print the Hand's total value
    def hand_total(hand):
        print("Hand Total : %d" % hand.total)
