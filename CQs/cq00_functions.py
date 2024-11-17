"""Functions challenge question."""

__author__ = "730654182"


def mimic(message: str) -> str:
    """Mimic takes in an input and repeats it."""
    return message


def main() -> None:
    """Prints the result of calling mimic."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
