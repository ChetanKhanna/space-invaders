class Defender(pygame.sprite.Sprite):
    """
    Defining the defender spaceships and its
    properties
    """
    def __init__(self,defender_image, x_pos, y_pos):
        super().__init__()
        
        self.image = pygame.image.load("defender.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (x_pos, y_pos))
        
    def left(self, movement):
        self.rect.x += movement # we will need a limit; if rect.x goes beyond that limit, 
                                # it will hit the wall or something and hence, won't increase
    def right(self, movement):
        self.rect.x -= movement
        
    def shoot(self):
        Missile.shoot() # missile is another class
                        # not sure, still
        
        
