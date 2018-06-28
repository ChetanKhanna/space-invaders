class Missiles(pygame.sprite.Sprite):
    """
    describing bullets; thinking to keep missils
    type same for everythnig - all alien ships and
    defender
    """
    def __init__(self, image_missile, x_pos, y_pos, direction, speed):
        
        super().__init__()
        self.image = image_missile
        self.rect = self.image.get_rect(topleft = (x_pos, y_pos))
        self.direction = direction
        self.speed = speed
        
    def shoot(self)
        # if it goes beyond certain dimension, self.kill()
        # self.rect.y += self.speed * self.direction
