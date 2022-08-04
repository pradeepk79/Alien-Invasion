class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Intialise the games settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # Ship Settings
        # Ship position is adjusted to 1.5 pixels rather than 1 pixel on each pass through the loop

        self.ship_speed = 1.5

        # Bullet Settings, values in pixels
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        # Create dark grey bullet
        self.bullet_color = (60, 60, 60)
        # Limiting the number of bullets the player can have
        self.bullets_allowed = 3
