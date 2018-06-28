class Blocks(pygame.sprite.Sprite):
    """
    Class for defining blocks and their properties;
    basically their damage rate.
    """
    def __init__(self, block_image):
        super.()__init__()
        self.image = block_image
        self.rect = self.image.get_rect()
        # or probably, just a simple rectangle object.
        # for i in range(self.height):
        #     for j in range(self.width):
        #         pygame.draw.rect(display, self.color,
        #                          self.small_area, width = 0)
        
        # This will basically give a rectangle of rectangles
        # We can then delete each smaller rectange as a
        # missile hits it. Not really sure how well it will
        # work though
        
    def damage(self):
        # a function to calculate damage to block
