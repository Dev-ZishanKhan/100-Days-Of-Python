import random

def deal_cards():
    """This will return a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Takes a list of cards and returns the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compare scores and return result"""
    if user_score > 21:
        return "You went over. You lose 😭"
    if computer_score > 21:
        return "Computer went over. You win 😁"
    if user_score == computer_score:
        return "Draw 🙃"
    elif user_score == 0:
        return "Blackjack! You win 😎"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score > computer_score:
        return "You win 😁"
    else:
        return "You lose 😤"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    # Computer plays only after user ends
    while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
        computer_cards.append(deal_cards())

    print(f"\nYour final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
    print(compare(calculate_score(user_cards), calculate_score(computer_cards)))

# Game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_game()
