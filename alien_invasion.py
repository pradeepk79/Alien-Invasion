# import sys module to exit the game if user quits by closing the window.
import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        # Create an instance of Scoreboard to store game statistics
        self.sb = Scoreboard(self)

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

        # Make the Play Button
        # Create an instance of Button with the label Play

        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        # Game is controlled by Run Game Method
        #  while loop contains an event loop
        # and code that manages screen updates.
        while True:

            # Isolate event management through helper method
            self._check_events()

            # Identify when parts of the game should run
            # To update the ships position
            if self.stats.game_active:
                self.ship.update()

                # To update position of bullets through the while loop
                # Call to update on group automatically calls update for each bullet
                # in the group bullets
                self._update_bullets()

                # To update alien position
                self._update_aliens()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        # Check for number of bullets fired by the player
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    # check key Up or released event

    def _check_keyup_events(self, event):
        """Respond to ker releases """
        # check key up or released is of right arrow key
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        # check key released of up is of left arrow key
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play."""
        # check wheather the point of mouse click overlaps the region defined
        # by the play buttons rect
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game statistics.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            # Prepare the scoreboard with zero score
            self.sb.prep_score()
            self.sb.prep_level()
            # To show the player how many ships to start with when new game starts.
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
        then Update the positions of all aliens in the fleet."""
        # use update method on aliens group which calls each alien's update()
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien ship collisions
        # The function looks for any member of group that has collided with the sprite
        # Stops looping through the group as soon as it finds one member that has collided with the sprite
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""

        if self.stats.ships_left > 0:
            # Decrement ships left and update scoreboard.
            self.stats.ships_left -= 1
            # update the display of ship images when the player loses a ship
            self.sb.prep_ships()

            # Get rid of remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Add Pause after update is made to all game elements but before any changes have been drawn to screen .
            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    # Check aliens that reach bottom of the screen

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this same as that as if ship got hit.
                self._ship_hit()
                break

    def _update_bullets(self):
        """Update positions of bullets and get rid of old bullets."""
        self.bullets.update()
        # Get rid of bullets that have disappeared.Create a copy of the group
        # We cant remove bullets from live loop
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        # The two True argument tells pygame to delete the bullets and aliens that have collided

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            # Any bullet that collides with alien is the key in collisions dictionary
            # Value associate with each bullet is a list of aliens it has collided with.
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            #  Call high score method each time an alien is hit after updating the score
            # check high score is called when the collision dictionary is present and
            # After updating the scores for all the aliens have been hit.
            self.sb.check_high_score()
        # Check if aliens group is empty, empty group evaluates to False
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            # Get rid of any existing bullets by using empty() method
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            # If fleet is destroyed, increment value of stats.level and call prep_level() to display the level
            self.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create one instance of Alien and add it to the group that hols the fleet of aliens.
        alien = Alien(self)
        # Find number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien_width, alien_height = alien.rect.size
        # Figure out how many aliens fit in a row, find out the horizontal space we have
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # To find number of aliens that fit across the screen
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            # Create the first row of aliens.
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height  = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    # Dropping the fleet and changing Direction

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        # Loop through the fleet and call check_edges() on each alien
        for alien in self.aliens.sprites():
            if alien.check_edges():
                # If check_edges() returns true call _change_fleet_direction()
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

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

        # Draw the score information.
        self.sb.show_score()


        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
