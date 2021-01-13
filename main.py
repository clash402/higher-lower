import random
from art import logo, vs
from game_data import data


# METHODS
def format_data(acc):
    return f"{acc['name']}, a {acc['description']} from {acc['country']}"


def find_most_popular(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "a"
    else:
        return "b"


def play():
    print(logo)
    game_is_in_progress = True

    while game_is_in_progress:
        score = 0
        round_is_in_progress = True
        b = random.choice(data)

        while round_is_in_progress:
            a = b
            b = random.choice(data)

            if a == b:
                b = random.choice(data)

            most_popular = find_most_popular(a, b)

            print(f"Compare A: {format_data(a)}")
            print(vs)
            print(f"Against B: {format_data(b)}")

            guess = input("\nWhich is more popular (A or B): ").lower()

            if guess == most_popular:
                score += 1
                print(f"You got it. Your current score is {score}")
            else:
                print(f"Nope. Your final score is {score}")
                round_is_in_progress = False

        if input("Play again? (y/n) ").lower() != "y":
            print("Goodbye")
            game_is_in_progress = False


# MAIN
play()
