# Secret Auction Biding
import os
bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders>? Type yes'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        os.system("cls")
highest_bid = 0
winner = ""
for bid in bids:
    value = bids[bid]
    if value > highest_bid:
        highest_bid = value
        winner = bid
print(f"The winner is {winner} with bid of ${highest_bid}")
