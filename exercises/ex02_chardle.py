"""EX02 - Chardle - A Cute Step Towad Wordle."""

__author__ = "730654182"


# Prompting for an input word
def input_word() -> str:
    """Prompts the user to input a 5-character word."""
    word = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        return word
        # exit()  # This exits the program if the word is not 5 characters long
    return word


# Prompting for an input character
def input_letter() -> str:
    """Prompts the user to input a single character."""
    letter = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        return letter
        # exit()  # Exits the program if more than one character is entered
    return letter


# Finding character matches and recording their positions.
def contains_char(word: str, letter: str) -> None:
    """This checks if the letter is present in the word and its counts matches."""
    print(f"Searching for {letter} in {word}")
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            print(f"{letter} found at index {i}")
            count += 1
    if count == 0:
        print(f"No instances of {letter} found in {word}")
    elif count == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{count} instances of {letter} found in {word}")


# The function that puts everything together.
def main() -> None:
    """Main function that runs the Chardle game."""
    word = input_word()
    letter = input_letter()
    contains_char(word, letter)


# The standard code to call the main function when running the script.
if __name__ == "__main__":
    main()
