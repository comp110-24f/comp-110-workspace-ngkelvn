"""My first wordle game!"""

__author__ = "730654182"


def input_guess(valid_length: int) -> str:
    """Prompts a user for a guess until it matches the required length."""
    guess = input(f"Enter a {valid_length} character word: ")
    while len(guess) != valid_length:
        guess = input(f"That wasn't {valid_length} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if the single character char_guess is in the secret_word."""
    assert len(char_guess) == 1  # Ensure char_guess is exactly 1 character
    i = 0
    while i < len(secret_word):
        if secret_word[i] == char_guess:
            return True
        i += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Return a string of emoji boxes representing the accuracy of the guess."""
    assert len(guess) == len(secret)
    emoji_result = ""
    i = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
        i += 1
    return emoji_result


def main(secret: str) -> None:
    """Main game loop for Wordle."""
    turns = 1
    won = False
    while turns <= 6 and not won:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)
        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            won = True
        else:
            turns += 1
    if not won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
