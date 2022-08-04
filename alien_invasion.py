# import sys module to exit the game if user quits by closing the window.
import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        # the function initializes the background settings that Pygame needs to work properly
        pygame.init()

        """Use call set mode to create a display window"""
        self.settings = Settings()
        # To run the game in full screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # import ship and create an instance of ship once the screen is created
        # Call to Ship class requires one argument, an instance of Alien Invasion,
        # self refers to current instance of Alien Invasion, gives Ship access to games resources such as screen object

        self.ship = Ship(self)
        # Create a group to store all live bullets to manage that is already fired
        # Bullets group will be instance of Sprite Group class which behaves like list
        self.bullets = pygame.sprite.Group()

        # Create a group to hold the fleet of aliens
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        # Game is controlled by Run Game Method
        #  while loop contains an event loop
        # and code that manages screen updates.
        while True:

            # Isolate event management through helper method
            self._check_events()
            # To update the ships position
            self.ship.update()
            # To update position of bullets through the while loop
            # Call to update on group automatically calls update for each bullet
            # in the group bullets
            self._update_bullets()
            # Update the screen
            self._update_screen()

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Check for Key down event
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # check key pressed is of right arrow key
    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # check key pressed is of left arrow key
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Pressing Q to quit the game
        elif event.key == pygame.K_q:
            sys.exit()
        # To fire bullet when space bar is pressed
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    # check key Up or released event
    def _check_keyup_events(self, event):
        """Respond to ker releases """
        # check key up or released is of right arrow key
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        # check key released of up is of left arrow key
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        # Check for number of bullets fired by the player
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update positions of bullets and get rid of old bullets."""
        self.bullets.update()
        # Get rid of bullets that have disappeared.Create a copy of the group
        # We cant remove bullets from live loop
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create one instance of Alien and add it to the group that hols the fleet of aliens.
        alien = Alien(self)
        # Find number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien_width = alien.rect.width
        # Figure out how many aliens fit in a row, find out the horizontal space we have
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # To find number of aliens that fit across the screen
        number_aliens_x = available_space_x // (2 * alien_width)

        # Create the first row of aliens.
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)

    def _create_alien(self, alien_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _update_screen(self):
        """Update images on the screen amd flip to new screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        # After filling the background, draw ship on the screen so ship appears on top of background
        self.ship.blitme()
        # Update to draw each bullets to the screen
        # bullets.sprites() returns a list of all sprites in the group bullets
        # To draw all fired bullets to the screen
        for bullet in self.bullets.sprites():
            # Call draw bullet on each one
            bullet.draw_bullet()

        # To make alien appear, we need to call the groups draw() method
        # draw() on group draws each element in the group at the position defined by its rect attribute
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
