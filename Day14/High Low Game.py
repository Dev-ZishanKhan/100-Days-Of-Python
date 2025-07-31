from data import data
import random

score = 0
game_should_continue = True
account_b = random.choice(data)

def data_format(account):
    """Format the account data into printable form."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Check if the user's guess is correct."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    # Avoid comparing the same person
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {data_format(account_a)}")
    print(f"Against B: {data_format(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.\n")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
