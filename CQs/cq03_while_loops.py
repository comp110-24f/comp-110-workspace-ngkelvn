"""Writing a function that counts the occurences of a character in a phrase."""

__author__ = "730654182"


def num_instances(phrase: str, search_char: str):
    """Takes in a phrase(string) and returns the number of insances it occurs."""

    count = 0  # Begins the counter
    index = 0  # Begins indexing

    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1

    return count
