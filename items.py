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

   
    def roll_damage(self) -> int:
        """
        Rolls the damage dice to determine the damage value.
        Returns an integer (the damage value).
        """
        return self.dice_damage.roll()

    