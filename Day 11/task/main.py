import random
import art
print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
comp = []
player = []

def total_value(hand):
    total = 0
    for card in hand:
        total += card
    return total

def human(cards):
    while True:
        if player == []:
            player.append(random.choice(cards))
            player.append(random.choice(cards))
            print("Your cards are: ", end = "")
            for card in player:
                print(card, end = " ")
            print()
        else:
            if total_value(player) > 21:
                break
            else:
                print(f"Current score: {total_value(player)}")
                y_or_n = input("Are you willing to draw a card from the deck(y/n)? ")
                if y_or_n == "y":
                    player.append(random.choice(cards))
                elif y_or_n == "n":
                    break
                else:
                    print("Enter a valid option")
                    continue

def computer(cards):
    while True:
        if comp == []:
            comp.append(random.choice(cards))
            comp.append(random.choice(cards))
        else:
            if total_value(comp) < 16:
                comp.append(random.choice(cards))
            else:
                break
    print("The first card of computer is", comp[0])

def result(human, computer):
    print("Your cards: ",human)
    print("Computer's cards: ",computer)
    if total_value(computer) > total_value(human):
        print("Computer wins!")
    if total_value(computer) < total_value(human):
        print("Human wins!")
    if total_value(human) == total_value(computer):
        print("Tie")

computer(cards)
human(cards)
result(player, comp)