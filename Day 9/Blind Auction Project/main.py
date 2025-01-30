import art
print(art.logo)
anymore_bidder_left=True
bid_dictionary={}

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    max_bid=0
    max_bid_person=""
    for bidder in bidding_dictionary:
        name_bid=bidding_dictionary[bidder]
        if name_bid>max_bid:
            max_bid=name_bid
            max_bid_person=bidder

    # maxBidPerson=max(bidding_dictionary,key=bidding_dictionary.get)
    print(f"The winner is {max_bid_person} with a bid of ${max_bid}")


while anymore_bidder_left:
    # TODO-1: Ask the user for input
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bid_dictionary[name]=bid
    # TODO-3: Whether if new bids need to be added
    any_bids_left=input("Are there any other bidders?Type 'yes' or "
                        "'no'.\n").lower()
    if any_bids_left!='yes':
        anymore_bidder_left=False
        find_highest_bidder(bid_dictionary)
    else:
        print("\n" * 20)



