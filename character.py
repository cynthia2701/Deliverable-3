# Task 1: update the character class

class Character: 


    def __init__(self, name: str, hp_max: int = 100, 
                 damage: int = 10, weapon: Weapon = None)-> None:
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
        """
        Returns HP of character as int. 
        """
        return self._hp

    
    @property
    def is_alive(self) -> bool:
        """
        Checks if character is alive, meaning HP > 0. 
        Returns True if alive, False if dead. 
        """
        return True if self._hp > 0 else False

 
    def take_damage(self, amount: int) -> None:
        """
        Reduces the characters HP by the specified amount/damage. 

        Args:
            amount (int): The amount of damage. 
        """
        self._hp -= amount
        self._hp = max(self._hp, 0)  # Makes sure HP doesn't go below 0


    def heal(self, amount: int) -> None:
        """
        Restores the chracters HP by the specified amount. 

        Args:
            amount (int): The amount of healing.
        """
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)  # Makes sure HP doesn't exceed max

    
    # from original script:
    # edited after task 3, including weapon: 
    def attack(self, target: 'Character') -> None:
        """
        Attack on another character, reducing their HP.
        Damage is either done by the characters weapon if they have one, 
        or by the characters base damage. 

        Args: 
            target (Character): The character being attacked.
        """
        if self.weapon is not None: 
            damage = self.weapon.roll_damage() #damage from weapon instad of default base damage. 
        else: 
            damage = self.damage #default base damage.  
        target.take_damage(damage)


    def introduce(self) -> str:
        """
        Introduces character. Returns string. 
        """
        return f"My name is {self.name}."


    def __repr__(self) -> str:
        """
        Representation of character with name, HP, damage. Returns string.
        """
        return f"Name = {self.name}, HP = {self.hp} Damage = {self.damage}."

    
    def __str__(self) -> str:
        """
        String representation of character. 
        """
        return f"Character is {self.name}, with {self.hp} HP and {self.damage} Damage."


#Task 04: Character specialization

class Warrior(Character):
    def __init__(self, name: str, hp_max: int = 100,
                 damage: int = 10, weapon=None,
                 armor: int = 5) -> None:
        """
        Create a Warrior character.

        Args:
            name (str): The name of the warrior.
            hp_max (int): Maximum HP, default is 100.
            damage (int): Base attack damage, default is 10.
            weapon (Weapon): Optional weapon, default is None.
            armor (int): Armor value, default is 5.
        """
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """
        Reduce incoming damage using the warrior's armor.

        Args:
            amount (int): Damage received before armor reduction.

        The armor value is subtracted from incoming damage.
        max() makes sure the damage cannot be negative.
        super().take_damage() updates the warrior's HP.
        """
        reduced_damage = max(0, amount - self.armor)
        super().take_damage(reduced_damage)


# Task 04. Mage is a subclass of Character.

class Mage(Character):
    def __init__(self, name: str, hp_max: int = 100,
                 damage: int = 10, weapon=None,
                 mana: int = 30, mana_max: int = 30) -> None:
        """
        Create a Mage character.

        Args:
            name (str): The name of the mage.
            hp_max (int): Maximum HP, default is 100.
            damage (int): Base attack damage, default is 10.
            weapon (Weapon): Optional weapon, default is None.
            mana (int): Available mana, default is 30.
            mana_max (int): Maximum mana, default is 30.
        """

        # Initialize attributes from Character.
        super().__init__(name, hp_max, damage, weapon)

        # Set the mage's mana and maximum mana.
        self.mana_max = mana_max
        self.mana = min(max(0, mana), mana_max)

    def attack(self, target: Character) -> None:
        """
        Attack another character using magic or a normal attack.

        Args:
        target (Character): The character being attacked.

        If the mage has at least 10 mana, it uses 10 mana to deal double base damage without using a weapon.
        If the mage has less than 10 mana, it uses a normal attack and restores 5 mana.

        Then the mana cannot exceed the maximum mana value.
        """
        # Use a magic attack if the mage has enough mana.
        if self.mana >= 10:
            self.mana -= 10

            # Magic deals double base damage without using a weapon.
            magic_damage = self.damage * 2
            target.take_damage(magic_damage)

        else:
            # Use a normal attack, including a weapon if equipped.
            super().attack(target)

            # Restore 5 mana without exceeding the maximum.
            self.mana = min(self.mana + 5, self.mana_max)