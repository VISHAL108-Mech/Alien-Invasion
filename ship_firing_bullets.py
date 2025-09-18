"""Creating a Pygame window and Responding to User Input"""
import pygame

class AlienInvasion:
    """Class for managing game resources and behavior."""

    def __init__(self):
        """Initialize/set up the game, and create game assets."""
        pygame.init() # 1 Initializes pygame's background settings.
        print("Pygame initialized.")

        self.screen = pygame.display.set_mode((1535, 785))
        pygame.display.set_caption("Alien Invasion")

    @staticmethod
    def run_game():
        """Start the main loop for the game."""
        running = True
        while running:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # Make the most recently drawn screen visible.
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
     # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
