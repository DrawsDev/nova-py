import pygame

class Window:
    def __init__(self, title: str, width: int, height: int):
        self.set_title(title)
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.Clock()
        self._delta = 0
        self._framerate = 30
        self._should_close = False
    
    def set_title(self, title: str):
        pygame.display.set_caption(title)

    def get_title(self) -> str:
        return pygame.display.get_caption()[0]

    def set_icon(self, surface: pygame.Surface):
        pygame.display.set_icon(surface)

    def set_framerate(self, framerate: float):
        self._framerate = framerate

    def get_framerate(self) -> float:
        return self.clock.get_fps()

    def get_delta(self) -> float:
        return self._delta

    def toggle_fullscreen(self):
        pygame.display.toggle_fullscreen()

    def is_fullscreen(self) -> bool:
        return pygame.display.is_fullscreen()

    def should_close(self) -> bool:
        return self._should_close

    def process(self):
        self._delta = self.clock.tick(self._framerate) / 1000
        self._should_close = pygame.event.get(pygame.QUIT)
        pygame.display.update()
