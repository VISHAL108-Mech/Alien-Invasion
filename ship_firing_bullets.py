"""Creating a Pygame window and Responding to User Input"""
import pygame

class AlienInvasion:
    """Class for managing game resources and behavior."""

    def __init__(self):
        """Initialize/set up the game, and create game assets."""
        pygame.init() # Initializes pygame's background settings.
        self.clock = pygame.time.Clock() # Creating a clock object to set FPS rate.
        self.screen = pygame.display.set_mode((1535, 784)) # Sets the background window in pixels.
        pygame.display.set_caption("Alien Invasion") # It shows the title of the game above the bar of the window.
        self.bg_color = (230, 230, 230) # Sets the background color.

    def run_game(self):
        """Start the main loop for the game."""
        running = True
        while running:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Redraw the screen and fill it with background color during each pass through the loop.
            self.screen.fill(self.bg_color)
            # Make the most recently drawn screen visible.
            pygame.display.flip() # Updates the screen and show's it to the player.
            self.clock.tick(60) # Tells the game to run at 60 FPS.
        pygame.quit()

if __name__ == "__main__": # It runs the file if its main not imported.
     # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
