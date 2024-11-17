"""Function to remove max value from a list"""

__author__ = "730654182"


# a function that will find and remove max of the list
def find_and_remove_max(a: list[int]) -> int:
    if len(a) == 0:
        return -1  # return value if the list is empty

    # Find the maximum value
    max_value = a[0]
    for num in a:  # iterate through each item in the list
        if num > max_value:
            max_value = num  # if number is bigger, replace max_value

    # Remove all occurrences of the max value by iterating backwards
    i = len(a) - 1
    while i >= 0:
        if a[i] == max_value:  # if the value is the max_value
            a.pop(i)
        i -= 1  # decreasing index

    return max_value
