# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
name = input("Enter your name: ")
bid = int(input("Enter your bid $"))
bidders = {}
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        if int(bidding_dictionary[bidder]) > highest_bid:
            highest_bid = bidding_dictionary[bidder]
            winner = bidder
        else:
            continue
    return winner
while True:
    loop = input("Anyone else interested in bid?(y/n) ")
    if loop == "y":
        print("\n" * 100)
        name = input("Enter your name: ")
        bid = input("Enter your bid $")
        bidders[name] = bid
    elif loop == "n":
        win = find_highest_bidder(bidders)
        print(f"The winner is : {win} and the highest bid is {bidders[win]}.")
        break
    else:
        print("Please enter either 'y' or 'n'.")

