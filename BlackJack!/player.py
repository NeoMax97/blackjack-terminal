import table
import numpy as np
import random


# Main function to be called from other files
def main():
    setup()
    return play.total


# Setting up initial variables for a fresh game
def setup():
    setup.money = 100
    setup.np_cards = table.setup.np_cards
    setup.no_of_cards = 0
    setup.cards_in_play = []
    setup.ace = 0
    setup.split = 0


# Handles betting by the player
def bet():
    bet_amount = random.randint(5, 100)
    while(bet_amount > setup.money):
        bet_amount = random.randint(5, 100)
    setup.money -= bet_amount
    return bet_amount


# Handling gameplay
def play():
    setup()
    play.bet_amount = bet()
    play.total = 0
    action = 1
    play.total += table.deal_cards(0)
    while (play.total < 21 and action == 1):
        play.total += table.deal_cards(0)
        check_split(setup.cards_in_play)
        action = action(play.total)


# Checks if splitting is possible
def check_split(hand):
    card1 = hand[0].split(" ")
    card2 = hand[1].split(" ")
    if (card1[1] == card2[1]):
        setup.split = 1


# Handles user-input for determining action
def action(total):
    if(setup.split == 1):
        if (total < 19):
            action = random.randint(1, 4)
        else:
            action = random.randint(2, 4)
    else:
        if (total < 19):
            action = random.randint(1, 3)
        else:
            action = random.randint(2, 3)
    return action


# Check function for dealing with action
def check_action(action):
    if (action == 1):
        return 1
    elif (action == 2):
        return 2
    elif(action == 3):
        surrender()
    else:
        split()


# Hnadles gameplay when hand is split
def split():
    if (setup.split == 1):
        split.hand1 = []
        split.hands1.append(setup.cards_in_play[0])

        card_value = table.get_value(split.hand1[0])
        card_value = table.letter_cards(card_value)

        split.total1 = int(card_value)

        split.hand2 = []
        split.hands2.append(setup.cards_in_play[1])

        card_value = table.get_value(split.hand1[1])
        card_value = table.letter_cards(card_value)

        split.total2 = int(card_value)

        command1 = 1
        command2 = 1

        while(split.total1 < 21 or split.total2 < 21):
            if (command1 == 1 or command2 == 1):
                if (split.hand1 != []):
                    # split.total1 += split_deal(1)
                    split.total1 += table.deal_cards(1)
                    table.draw_card(split.hand1, len(split.hand1))
                if (split.hand2 != []):
                    # split.total2 += split_deal(2)
                    split.total2 += table.deal_cards(2)
                    table.draw_card(split.hand2, len(split.hand2))

            for cards in split.hand1:
                if(table.get_value(cards) == "A"):
                    choose_ace(1, split.hand1)
            for cards in split.hand2:
                if(table.get_value(cards) == "A"):
                    choose_ace(1, split.hand2)
        split_check(split.total1, split.total2)


# Handles surrender
def surrender():
    setup.money += (play.bet_amount / 2)
