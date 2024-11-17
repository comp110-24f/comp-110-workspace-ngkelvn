"""Writing A Simple Number Guessing Game!"""

__author__ = "730654182"


def guess_a_number() -> None:
    secret = 7
    user_guess = input("Guess a number: ")
    print(f"Your guess was {user_guess}")

    if int(user_guess) == secret:
        print("You got it!")
    elif int(user_guess) < secret:
        print(f"Your guess was too low! The secret number is {secret}")
    else:
        print(f"Your guess was too high! The secret number is {secret}")


if __name__ == "__main__":
    guess_a_number()
