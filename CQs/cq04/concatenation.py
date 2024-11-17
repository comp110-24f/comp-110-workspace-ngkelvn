"""Concatinating two strings."""

__author__ = "730654182"


def concat(str1: str, str2: str) -> str:
    return str1 + str2


# Global variables
word1 = "happy"
word2 = "tuesday"


if __name__ == "__main__":  # suppresses the function call on import.
    # prints results of calling concat with word1 and word2
    print(concat(word1, word2))
