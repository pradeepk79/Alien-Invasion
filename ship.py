import pygame

class Ship:
    """A class to manage the ship"""

    #Ship takes two parameters: the self reference and a reference to the current instance of the AlienInvasion
    # This will give ship access to all the game resources defined in alien invasion

    def __init__(self, ai_game):
            """Initialize the ship ans set its starting position"""
            #assign screen to attribute of ship to access all the methods in this calss
            self.screen = ai_game.screen

            #access screens rectangle to place the ship in correct location on the screen
            self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect and give location of ship
            self.image = pygame.image.load('images/ship.bmp')
            self.rect = self.image.get_rect()

        # Start the new ship at bottom center of the screen
            self.rect.midbottom = self.screen_rect.midbottom

        # Draw the ship at its current location

    def blitme(self):
                """Draw the ship to the screen at the position specified by self.rect"""
                self.screen.blit(self.image, self.rect)
