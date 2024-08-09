from game_data1 import data
import random
from art import logo,vs

def get_random_account():
    return random.choice(data)

def data_info(account):
    name = account["name"]
    acc_desc = account["description"]
    acc_country = account["country"]
    return f"{name}, a {acc_desc} , from {acc_country}"

def check_answer(guess, acc_a_followers, acc_b_followers):
    if acc_a_followers > acc_b_followers:
        if guess == "a":
            return True
        else:
            return False
    elif acc_a_followers < acc_b_followers:
        if guess == "b":
            return True
        else:
            return False

    #     return guess == "a"
    # else:
    #     return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_b = get_random_account()
    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()
        print(f"Compare A: {data_info(account_a)}")

        print(vs)

        print(f"Against B: {data_info(account_b)}")

        guess = input("Who is higher, Type 'A' or 'B': ").lower()
        acc_a_followers = account_a["follower_count"]
        acc_b_followers = account_b["follower_count"]

        is_correct = check_answer(guess,acc_a_followers,acc_b_followers)

        if is_correct:
            print(logo)
            score += 1
            print(f"You got it right!, Your current score is {score}")
        else:
            print(f"You got the wrong one!, Your final score is {score}")
            game_should_continue = False

game()











