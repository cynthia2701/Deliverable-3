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


    def roll(self) -> int: 
        """
        Rolls dice to return a random number
        between 1 and the maximum number of sides on the dice. 
        Returns an integer. 
        """
        return random.randint(1, self.sides)

 
    def __repr__(self) -> str: 
        """
        Returns a string saying the number of sides on the dice
        """
        return f"Dice (sides={self.sides})"

    
    def __call__(self) -> int: 
        """
        Rolls the dice when called like a function.
        Returns an integer.
        """
        return self.roll()
        