# Task 1: update the character class

class Character: 
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon = None) -> None:
        """
        Character creation.

        Args: 
            name (str): The name of the character.
            hp_max (int): The maximum health points. Set to 100. 
            damage (int): The damage the character can deal. Set to 10.
            weapon (Weapon): Optional weapon for character. Set to None default. 
        """
        self.name = name
        self._hp = hp_max
        self.weapon = weapon
        self.hp_max = hp_max
        self.damage = damage

    @property #only allows reading, no editing of value.
    def hp(self) -> int:
        return self._hp
    
    # is_alive method added to check if HP is above 0. If not, character is dead. 
   
    @property
    def is_alive(self) -> bool:
        return True if self._hp > 0 else False

    # take_damage added to reduce characters HP when injured. 
    def take_damage(self, amount: int) -> None:
        self._hp -= amount
        self._hp = max(self._hp, 0)  # Makes sure HP doesn't go below 0

    # heal method added when character heals and HP goes up.
    def heal(self, amount: int) -> None:
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)  # Makes sure HP doesn't exceed max

    # from original script:

    # edited after task 3, including weapon: 
    def attack(self, target: 'Character') -> None:
        if self.weapon is not None: 
            damage = self.weapon.roll_damage() #damage from weapon instad of default base damage. 
        else: 
            damage = self.damage #default base dagame. 
        target.take_damage(damage)

    def introduce(self) -> str:
        return f"My name is {self.name}."

    def __repr__(self) -> str:
        return f"Name = {self.name}, HP = {self.hp} Damage = {self.damage}"
    
    def __str__(self) -> str:
        return f"Character: Name = {self.name}, HP = {self.hp}, Damage = {self.damage}"