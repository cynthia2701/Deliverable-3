# Task 2: Introducing randomness with a Dice class
import random

class Dice: 
    def __init__(self, sides: int = 6) -> None:
        """
        Dice creation including number of sides.

        Args:
            sides (int): The number of sides on the dice. 
            Default number of sides is 6.
        """

        if sides < 2: 
            raise ValueError("Sides must be two or more.")
        self.sides = sides

    # roll method added to return a number between 1 
    # and the number of sides on the dice. 
    def roll(self) -> int: 
        return random.randint(1, self.sides)

    # __repr__ makes it so the dice can be represented as a string 
    # showing the number of sides on the dice.
    def __repr__(self) -> str: 
        return f"Dice (sides={self.sides})"

    # __call__ makes it so dice can be called like a function to be 
    # able to roll it. 
    def __call__(self) -> int: 
        return self.roll()
        