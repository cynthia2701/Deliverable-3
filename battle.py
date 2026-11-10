from character import Character


class Battle:
    """
    Manage a turn-based battle between two characters.
    """

    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Create a battle between a hero and an enemy.

        Args:
            hero (Character): The character who attacks first.
            enemy (Character): The character who attacks second.
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """
        Play one round of combat.

        The hero attacks first. If the enemy is still alive,
        the enemy attacks the hero.
        """
        if self.hero.is_alive and self.enemy.is_alive:
            self.hero.attack(self.enemy)

            if self.enemy.is_alive:
                self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """
        Continue playing rounds until one character is defeated.
        """
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()