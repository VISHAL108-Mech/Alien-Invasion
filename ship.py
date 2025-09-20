import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/FighterPlaneV2.bmp")
        self.rect = self.image.get_rect()

        # Placing the ship at mid-bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.speed

    def draw(self):
        """Draw the ship."""
        self.screen.blit(self.image, self.rect)
