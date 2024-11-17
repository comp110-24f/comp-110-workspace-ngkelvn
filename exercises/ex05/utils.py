__author__ = "730654182"


def only_evens(a: list[int]) -> list[int]:
    """Returns a list of only the even numbers from the input list."""
    result: list[int] = []
    for x in a:
        if x % 2 == 0:
            result.append(x)
    return result


def sub(a: list[int], start: int, end: int) -> list[int]:
    """Returns a subset of a list from start index to end index (not inclusive)."""
    if len(a) == 0 or start >= len(a) or end <= 0:
        return []

    if start < 0:
        start = 0
    if end > len(a):
        end = len(a)

    result: list[int] = []
    for i in range(start, end):
        result.append(a[i])

    return result


def add_at_index(a: list[int], value: int, index: int) -> None:
    """Modifies the list by adding the value at the specified index."""
    if index < 0 or index > len(a):
        raise IndexError("Index is out of bounds for the input list")

    a.append(0)  # Temporarily expand the list.
    i = len(a) - 1
    while i > index:
        a[i] = a[i - 1]
        i -= 1
    a[index] = value
