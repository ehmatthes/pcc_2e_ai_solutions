import pygame
from pygame.sprite import Sprite
 
class Raindrop(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, rd_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        # Load the raindrop image and set its rect attribute.
        #   Raindrop image from: https://commons.wikimedia.org/wiki/File:Antu_raindrop.svg
        #   License: https://creativecommons.org/licenses/by-sa/3.0/deed.en
        #   Modified size, and cropped.
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact vertical position.
        self.y = float(self.rect.y)

    def update(self):
        """Move the raindrop down the screen."""

        # Bug: This code makes all rows occupy the same position
        #   as the first row. I can't figure out why.
        #   self.y should be an instance variable, unique to each indivdual
        #   drop instance. But they all take the value of the first drop.
        #   Even if I write the update loop myself instead of calling it
        #   on the group, I get the same issue. If you can sort this out, 
        #   please let me know! ehmatthes at gmail :)
        # self.y += self.settings.raindrop_speed
        # self.rect.y = self.y

        # Updating the rect directly works.
        #   We lose the fine control of tracking position with a float, though.
        self.rect.y += self.settings.raindrop_speed
 
