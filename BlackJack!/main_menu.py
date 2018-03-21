from game import Game
from rules import Rules


class Main_Menu(object):

    def main(self):
        print("\nHi! Welcome to BlackJack!\n")
        print("S - Start a new game\n")
        print("R - Rules of the game\n")
        print("Q - Quit\n")

        option = input("What would you like to do?\n")

        if (option == "S" or option == "s"):
            game = Game()
            game.play()
        elif(option == "R" or option == "r"):
            rules = Rules()
            rules.main(self)
        elif(option == "Q" or option == "q"):
            exit(0)


menu = Main_Menu()
menu.main()
