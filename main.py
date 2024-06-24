from replit import clear

from art import logo

print(logo)

name = []
bid = []

more_people = True
while more_people:
    name.append(input("What is your name?: "))
    bid.append (int(input("What is your bid?: $")))
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders == "yes":
      clear()
    elif more_bidders == "no":
      more_people = False
highest_bid = bid.index(max(bid))
print(f"The winner is {name [highest_bid]} with a bid of ${max(bid)}") 


#Alternate code method using dictionaries:

# from replit import clear

# from art import logo

# print(logo)

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()