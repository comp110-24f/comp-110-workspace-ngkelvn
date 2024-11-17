"""Planning a cozy tea party!"""

__author__ = "730654182"


def main_planner(guests: int) -> None:
    """Denotes the number of guests attending the tea party."""

    print(f"A Cozy Tea Party for {guests} people!")
    print(f"Tea Bags: {tea_bags(people=guests)}")
    print(f"Treats: {treats(people=guests)}")
    print(f"Cost: ${cost(tea_bags(people=guests), treats(people=guests))}")


def tea_bags(people: int) -> int:
    """Denotes the number of tea bags each person takes."""
    return people * 2  # Returns the number of tea bags each person takes.


def treats(people: int) -> int:
    """Denotes the number of treats needed per tea consumed."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of tea bags and treats"""
    return (tea_count * 0.5) + (treat_count * 0.75)  # Calculates the total cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
