#Task 3: Create items
from dice import Dice

class Weapon: 
    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Weapon creation.

        Args:
            name (str): Name of the weapon.
            damage_dice (Dice): The dice used to determine damage.
        """
        self.name = name
        self.dice_damage = damage_dice

    # roll_damage method added to roll the dice and 
    # return the damage value.
    def roll_damage(self) -> int:
        return self.dice_damage.roll()

    