"""File to define River class."""

from ex07.fish import Fish
from ex07.bear import Bear


class River:
    """Makes a river ecosystem."""

    day: int
    bears: list[Bear] = list()
    fish: list[Fish] = list()

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = list()
        self.bears: list[Bear] = list()
        # populate the river with fish and bears
        for i in range(0, num_fish):
            self.fish.append(Fish())
        for i in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages of fishes and bears."""
        new_fish: list[Fish] = list()
        new_bears: list[Bear] = list()
        for x in range(0, len(self.fish)):
            if self.fish[x].age <= 3:
                new_fish.append(self.fish[x])
        for x in range(0, len(self.bears)):
            if self.bears[x].age <= 5:
                new_bears.append(self.bears[x])
        self.fish = new_fish
        self.bears = new_bears
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes a certain number of fish."""
        for i in range(amount):
            if self.fish:
                self.fish.pop(0)
            else:
                break

    def check_hunger(self):
        """Checking the hunger of each bear because when HS < 0, they starve."""
        surviving: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:  # keep the bear if HS > 0
                surviving.append(bear)
            self.bears = surviving
        return None

    def repopulate_fish(self):
        """Modeling reproduction for fish."""
        num_fish: int = (len(self.fish) // 2) * 4
        for i in range(0, num_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Modeling reproduction for bears."""
        num_bears: int = len(self.bears) // 2
        for i in range(0, num_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Viewing the population of fish and bear each day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        self.day += 1  # Increase day by 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
            # Simulate one day for all Fish
            for fish in self.fish:
                fish.one_day()
                # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        return None

    def one_river_week(self):
        """Simulate one week of life in the river."""
        i = 0
        while i < 7:
            River.one_river_day(self)
            i += 1
        return None

    def remove_fish(self, amount: int):
        """Method for removing fish."""
        for i in range(0, amount):
            self.fish.pop(i)
        return None
