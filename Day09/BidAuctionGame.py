### This is a simple auction game where users can bid on items.
def highest_bidder(total_bids):
    highest_bid=0
    winner=""
    for key in total_bids:    
        bid_amount=int(total_bids[key])                 
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=key

    print(f"\nWinner is {winner} with highest bid {highest_bid}")
        
total_bids={}       
while True:
    name=input("What is Your Name: ")
    bid=input("whats your bid: $")
    total_bids[name]=bid
    choice=input("Is there any other person want to bid Y/N: ").lower()
    if choice=="y":
        print("\n"*50)
    elif choice=="n":
        highest_bidder(total_bids)
    else:
        print("Invalid Choice...")
        break




