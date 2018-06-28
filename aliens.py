class Aliens(pygame.sprite.Sprite):
    """
    class for alien spaceship and their
    properties. We need to create a list of
    lists of objects of this class Aliens probably.
    """
    def __init__(self, ships, alien_image, x_pos, y_pos):
        super().__init__()
        
        self.image = alien_image
        self.rect = self.image.get_rect(topleft = (x_pos, y_pos)) 
            
    def move_down(self, movement):
        # to make the ship come down
        
    def move_horizontal(self, movement): 
        # to make ship oscilate horizontally
        
    def shoot(self):
        # not all ships will shoot at once, we need to randomly select some of them
        # and call the Missile.shoot function or something to make them shoot
