import pygame

class Input:
    def __init__(self):
        pass

    def pressed(self, keycode: int) -> bool:
        return pygame.key.get_pressed()[keycode]
    
    def just_pressed(self, keycode: int) -> bool:
        return pygame.key.get_just_pressed()[keycode]
    
    def released(self, keycode: int) -> bool:
        return not self.pressed(keycode)

    def just_released(self, keycode: int) -> bool:
        return pygame.key.get_just_released()[keycode]
