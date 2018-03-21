class Rules(object):

    def main(self, menu):
        with open('rules.txt') as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]

        for line in lines:
            print(line + "\n")

        print("\n")
        val = input("Press any button to go back to Main Menu:")
        if val:
            menu.main()
