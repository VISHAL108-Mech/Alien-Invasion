class Settings:
    """A class to store game settings."""

    def __init__(self):
        """Initialize the game settings."""
        self.screen_width = 1500
        self.screen_height = 780
        self.bg_color = (0, 0, 0)
        self.speed = float(10)

        # Bullet settings
        self.bullet_speed = float(11)
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 213, 128)
        self.bullets_allowed = 3
