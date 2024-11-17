"""Utility functions for dictionary exercises."""

__author__ = "730654182"


def invert(given: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of the dictionary."""
    new_dict = {}
    for key, value in given.items():
        if value in new_dict:
            raise KeyError("Duplicate values found when inverting dictionary.")
        new_dict[value] = (
            key  # The new key is the old value, and the new value is the old key
        )
    return new_dict  # Return the new dictionary


def favorite_color(input: dict[str, str]) -> str:
    """Return the color that appears most frequently. In case of a tie, return the first occurring color."""
    color_name: str = ""
    result: dict[str, int] = {}  # Dictionary to store color and frequency

    for elem in input.values():  # Count occurrences of each color
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1

    color_name = ""
    for elem in result:
        if (
            color_name == ""
            or result[elem] > result[color_name]
            or (
                result[elem] == result[color_name]
                and list(input.values()).index(elem)
                < list(input.values()).index(color_name)
            )
        ):
            color_name = (
                elem  # Update the most frequent color with correct tie-breaking
            )

    return color_name  # Return the most popular color


def count(given_list: list[str]) -> dict[str, int]:
    """Count occurrences of each item in the list and return a dictionary of counts."""
    value_count: dict[str, int] = {}  # Create a dictionary to store counts
    for item in given_list:
        if item in value_count:
            value_count[
                item
            ] += 1  # Increment count if item is already in the dictionary
        else:
            value_count[item] = 1  # Initialize count if item is seen for the first time
    return value_count  # Return the resulting dictionary


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Organize words by their starting letter into a dictionary."""
    alpha_dict: dict[str, list[str]] = {}  # Create a new dictionary

    for elem in input_list:  # Iterate through each element
        first_letter = elem[0].lower()  # Find the lowercase value of the first letter
        if (
            first_letter in alpha_dict
        ):  # If this letter is a key already in the dictionary
            alpha_dict[first_letter].append(elem)  # Add this word to the list
        else:
            alpha_dict[first_letter] = [elem]  # Make a new list for this letter

    # Ensure each list of words is sorted alphabetically before returning
    for letter in alpha_dict:
        alpha_dict[letter] = sorted(alpha_dict[letter])  # Sort and reassign each list

    return alpha_dict  # Return the dictionary


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Update the attendance log by adding a student to a specific day without duplicating."""
    if day not in attendance_log:
        attendance_log[day] = []  # If the day is not in the log, create a list for it
    if (
        student not in attendance_log[day]
    ):  # Check if the student is already listed for that day
        attendance_log[day].append(student)  # Add the student if not already present
