class Command(object):

    # Function that handles user input to progress the game
    def action(self, hand, game):
        print("What would you like to do now?\n")
        print("1 - Hit\n")
        print("2 - Stand\n")
        print("3 - Surrender\n")

        self.cmd = int(input(""))
        if (self.cmd != 1 and self.cmd != 2 and self.cmd != 3):
            self.cmd = int(input("Invalid option. Please try again.\n"))

        if (self.cmd == 2):
            self.stand(game, hand)
        elif (self.cmd == 3):
            self.surrender(game)
        return self.cmd

    # Function that handles the Hit option
    def hit(self, hand, card):
        hand.add_card(card)

    # Function that handles the Stand option
    def stand(self, game, hand):
        hand.in_play = False
        print("- - - Stand - - -\n")

        if(game.dealer.hand.total == 21):
            if(game.hand.total == 21):
                game.money.balance += game.money.bet_amt
                game.dealer.money.balance += game.dealer.money.bet_amt
                print("! ! ! BLACKJACK ! ! ! \n")
                print("! Dealer got BLACKJACK ! \n")
                print("Split winnings with dealer\n")
            else:
                game.dealer.money.balance += (game.money.bet_amt * 2)
                print("! Dealer got BLACKJACK ! \n")
        else:
            if (game.hand.total > game.dealer.hand.total):
                game.money.balance += (game.money.bet_amt * 2)
                print("You won this round!\n")
            elif ((game.hand.total < game.dealer.hand.total) and game.dealer.hand.total <= 21):
                game.dealer.money.balance += (game.money.bet_amt * 2)
                print("The Dealer won this round!\n")
            else:
                game.dealer.money.balance += game.dealer.money.bet_amt
                game.money.balance += game.money.bet_amt
                print("* * * DRAW * * * ")

    # Function that handles the Surrender option
    def surrender(self, game):
        game.game_over = True
        print("x x x Surrender x x x\n")
        game.money.add(game.money.bet_amt / 2)
