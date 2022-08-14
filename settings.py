class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initialise the games static settings"""

        # Screen Settings

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # Ship Settings

        # Number of ships left
        self.ship_limit = 3

        # Bullet Settings, values in pixels

        self.bullet_width = 300
        self.bullet_height = 15
        # Create dark grey bullet
        self.bullet_color = (60, 60, 60)
        # Limiting the number of bullets the player can have
        self.bullets_allowed = 3

        # Alien settings

        # To control how fast the alien fleet drops down when it its the either
        # edge of the screen
        self.fleet_drop_speed = 10

        # How quickly the game speed up
        self.speedup_scale = 1.1

        # How quickly the alien point value increases
        self.score_scale = 1.5

        # to initialize the values of attributes that needs to be changed throughout the game
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throught the game"""
        # Ship position is adjusted to 1.5 pixels rather than 1 pixel on each pass through the loop

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Scoring
        self.alien_points = 50


        # fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values each time the player reaches new level."""
        # Increase games tempo by calling increase_speed()
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        # Rate at which the points increase
        self.alien_points = int(self.alien_points * self.score_scale)







