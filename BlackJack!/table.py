import numpy as np
import random


# Main function that handles gameplay
def game():
    # n_decks = input("\nHow many decks would you like to play with? \n")
    # print("How many players do you want to play with?
    # (Dealer not included)\n")
    # n_players = input()

    # Setup all variables for a new game
    setup()
    # Get bet amount
    game.bet_amount = bet()
    # Deal the card
    game.total = 0
    game.total += deal_cards(0)
    command = 1
    while(game.total < 21 and command == 1):
        game.total += deal_cards(0)
        # draw_card(deal.suit, deal.value)
        draw_card(setup.cards_in_play, len(setup.cards_in_play))
        view_info(setup.money, game.bet_amount)
        choose_ace(0, setup.cards_in_play)
        check_split()
        if (game.total == 21):
            print("! ! ! BLACKJACK ! ! ! ")
            break
        elif(game.total > 21):
            print("X X X BUST X X X")
            break
        action = hit_stand_surrender()
        command = check_action(action)
    # total = deal


# Gets input for Hit / Stand / Surrender / Split
def hit_stand_surrender():
    if(setup.split == 0):
        print("What would you like to do now?\n")
    print("1 - Hit\n")
    print("2 - Stand\n")
    print("3 - Surrender\n")
    if (setup.split == 1 and setup.split2 == 0):
        print("4 - Split")
    action = input("")
    return action


# Handles surrender by the player
def surrender():
    print("--- Surrender ---")
    setup.money += (game.bet_amount / 2)
    view_info(setup.money, game.bet_amount)


# Handles stand by the player
def stand():
    print("- - - Stand - - - ")
    view_info(setup.money, game.bet_amt)


# Checks if split is an option
def check_split():

    card1_value = get_value(setup.cards_in_play[0])
    card2_value = get_value(setup.cards_in_play[1])

    if (card1_value == card2_value):
        setup.split = 1


# Handles gameplay when hand is split
def split():
    split.hand1 = []
    split.hand1.append(setup.cards_in_play[0])
    card_value = get_value(split.hand1[0])
    card_value = letter_cards(card_value)

    split.total1 = int(card_value)

    split.hand2 = []
    split.hand2.append(setup.cards_in_play[1])
    card_value = get_value(split.hand2[0])
    card_value = letter_cards(card_value)

    split.total2 = int(card_value)

    command1 = 1
    command2 = 1

    while (split.total1 < 21 or split.total2 < 21):
        if (command1 == 1 or command2 == 1):
            if (split.hand1 != []):
                # split.total1 += split_deal(1)
                split.total1 += deal_cards(1)
                draw_card(split.hand1, len(split.hand1))
            if (split.hand2 != []):
                # split.total2 += split_deal(2)
                split.total2 += deal_cards(2)
                draw_card(split.hand2, len(split.hand2))
            view_info(setup.money, game.bet_amount)

        for cards in split.hand1:
            if(get_value(cards) == "A"):
                choose_ace(1, split.hand1)
        for cards in split.hand2:
            if (get_value(cards) == "A"):
                choose_ace(2, split.hand2)

        split_check(split.total1, split.total2)

        if (split.hand1 != []):
            print("What would you like to do with Hand 1?")
            action1 = hit_stand_surrender()
            command1 = check_action(action1)
            # draw_card(split.hand1, len(split.hand1))
            # draw_card(split.hand2, len(split.hand2))
            split_check(split.total1, split.total2)

        if (split.hand2 != []):
            print("What would you like to do with Hand 2?")
            action2 = hit_stand_surrender()
            command2 = check_action(action2)
            # draw_card(split.hand1, split.cards1)
            # draw_card(split.hand2, split.cards2)
            split_check(split.total1, split.total2)


# Checks if either hand has reached 21 or got busted
def split_check(total1, total2):
    if (total1 == 21):
        print("Hand 1 has reached 21. No BlackJack because of splitting.")
        split.hand1 = []
    if(total2 == 21):
        print("Hand 2 has reached 21. No BlackJack because of splitting.")
        split.hand2 = []
    if(total1 > 21 and total2 > 21):
        print("Both hands are BUSTED. Round Over. ")
        split.hand1 = []
        split.hand2 = []
    if (total1 > 21):
        print("Hand 1 is BUSTED. Hand 2 is left.")
        split.hand1 = []
    if (total2 > 21):
        print("Hand 2 is BUSTED. Hand 1 is left.")
        split.hand2 = []


# Handles the choosing of Ace card's value
def choose_ace(hand, cards_in_hand):
    for cards in cards_in_hand:
        # card = cards.split(" ")
        # if card[1] == "A" and setup.ace == 0:
        if (get_value(cards) == "A" and setup.ace == 0):
            if(hand == 0):
                print("You have an ACE! Would like to use it as 11 or 1?\n")
            elif(hand == 1):
                print("You have an ACE in Hand 1!")
                print("Would like to use it as 11 or 1?\n")
            elif(hand == 2):
                print("You have an ACE in Hand 2!")
                print("Would like to use it as 11 or 1?\n")

            value = input()
            while (value != "1" and value != "11"):
                print("Invalid option. Please try again.\n")
                value = input()
            if(hand == 0):
                game.total -= 11
                game.total += int(value)
            elif(hand == 1):
                split.total1 -= 11
                split.total1 += int(value)
            elif(hand == 2):
                split.total2 -= 11
                split.total2 += int(value)

    setup.ace = 1


# Calls corresponding function based on user-input
def check_action(action):
    if (action == "1"):
        print("\nHit!\n")
    elif(action == "2"):
        print("\nStand!\n")
    elif(action == "3"):
        # print("\nSurrender!\n")
        surrender()
    elif(action == "4" and setup.split == 1 and setup.split2 == 0):
        # print("\nSplit!\n")
        split()
    else:
        print("Please enter a valid command: \n")
        if (setup.split == 1):
            action = hit_stand_surrender()
        else:
            action = hit_stand_surrender()
        check_action(action)
    return int(action)


# Handles betting and deducting money from pool
def bet():
    bet_amount = int(input("\nPlease place your bet (between $5 and $100):\n"))
    while(bet_amount > setup.money):
        bet_amount = int(input("\nNot enough money. Please try again."))

    while(bet_amount < 5 or bet_amount > 100):
        print("\nBet out of bounds")
        bet_amount = input("\nPlease place your bet (between $5 and $100):\n")
        bet_amount = int(bet_amount)
    setup.money -= bet_amount

    return bet_amount


# Handles Dealing of cards to corresponding hand
def deal_cards(hand):
    # Choose a random card
    index = random.randint(0, 51)
    # If chosen card is already dealt, choose an undealt card
    while(setup.np_cards[index] == "0"):
        print("Index = %d" % index)
        index = random.randint(0, 51)
    # Deal the card
    card = setup.np_cards[index]
    # Store the card

    # Split suit and value from the card
    print("Card = " + card)
    deal_cards.suit = get_suit(card)
    deal_cards.value = get_value(card)
    # Add the card to the correct hand
    if (hand == 0):
        setup.cards_in_play.append(card)
        # setup.no_of_cards += 1
    elif(hand == 1):
        split.hand1.append(card)
    elif(hand == 2):
        split.hand2.append(card)

    # Get numerical value for return value
    number = int(letter_cards(deal_cards.value))
    # Remove the dealt card from the deck
    setup.np_cards[index] = "0"
    # Draw the card on the table
    # draw_card(suit, value)
    return number


# Handles setting numeric value of cards with letter values
def letter_cards(value):
    if(value == "A"):
        return 11
    elif(value == "J" or value == "Q" or value == "K"):
        return 10
    else:
        return int(value)


# Handles drawing of cards
def draw_card(cards, number):
    for i in range(number):
        print(" _ _ _ _ _    ", end="")
    print("\n")
    for card in cards:
        suit = get_suit[card]
        value = get_value[card]
        print("|%s        |   " % value, end="")
    print("\n")
    for card in cards:
        suit = get_suit[card]
        value = get_value[card]
        print("|    %s    |   " % suit, end="")
    print("\n")
    for card in cards:
        suit = get_suit[card]
        value = get_value[card]
        print("|        %s|   " % value, end="")
    print("\n")
    for i in range(number):
        print(" - - - - -    ", end="")
    print("\n")


# Setup of initial variables for a fresh game
def setup():
    setup.money = 100
    setup.ace = 0
    setup.split = 0
    setup.split2 = 0
    setup.cards_in_play = []

    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["♠", "♣", "♦", "♥"]
    deck = []
    for suit in suits:
        for value in values:
            deck.append(suit + " " + value)
    setup.np_cards = np.array(deck)
    # np_deck = no_of_decks * np_cards


# Display important info like Bet Amount and Money Left
def view_info(money, bet_amt):
    print("Money left : %d | Bet amount : %d" % money, bet_amt)


# Main function called in another file to start this file
def main():
    print("\nStarting a new game now")
    game()


# -------- Getters --------

# Returns the suit of the card as a string
def get_suit(card):
    suit_value = card.split(" ")
    return suit_value[0]


# Returns the numeric value of the card as a string
def get_value(card):
    suit_value = card.split(" ")
    return suit_value[1]
