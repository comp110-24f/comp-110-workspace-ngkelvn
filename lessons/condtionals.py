"""Practicing my conditionals."""

# def less_than_10(num: int) -> None:
#  """Tells us if a num < 10."""
# else:
# print("Big number!")
# print(less_than_10(num=20))


def check_first_letter(word: str, letter: str) -> str:
    if letter == word[0]:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="m"))
