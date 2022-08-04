import pygame


class Ship:
    """A class to manage the ship"""
    # ship takes two parameters: the self reference and a reference to the current instance of the AlienInvasion
    # This will give ship access to all the game resources defined in alien invasion

    def __init__(self, ai_game):
        """Initialize the ship ans set its starting position"""
        # assign screen to attribute of ship to access all the methods in this calss
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # access screens rectangle to place the ship in correct location on the screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect and give location of ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start the new ship at bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for ships horizontal position
        self.x = float(self.rect.x)

        # Ship Movement Flag when moving right and is motionless
        self.moving_right = False

        # Ship Movement Flag when moving right and is motionless
        self.moving_left = False

    def update(self):
        """Update ships position based on the status of Movement Flag along the Right direction"""
        # Ship stops moving with it reaches the right edge of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Update ships x value not the rect along right
            self.x += self.settings.ship_speed

        """Update ships position based on hte status of Movement Flag along hte Left direction"""
        # Ship stops moving with it reaches the left edge of the screen
        if self.moving_left and self.rect.left > 0:
            # Update ships x value not the rect along left
            self.x -= self.settings.ship_speed

            # Update rect object from self.x
            # self.rect.x will store only the integer portion of self.x value
        self.rect.x = self.x


    def blitme(self):
        """Draw the ship to the screen at the position specified by self.rect"""
        self.screen.blit(self.image, self.rect)
