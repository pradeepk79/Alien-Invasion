# import pygame to render text on screen
import pygame.font

# Creating a Button Class
class Button:

    # msg contains buttons text message
    def __init__(self, ai_game, msg):

        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        # None tells Pygame to use default font
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Render the string to display as an image
        # The button message needs to be prepared only once.
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    # Drawing the Button to the Screen

    def draw_button(self):
        # Draw blank button and then draw message.
        # call screen.fill to draw rectangular portion of the button
        self.screen.fill(self.button_color, self.rect)
        # call screen.blit() to draw the text image to the screen
        self.screen.blit(self.msg_image, self.msg_image_rect)




