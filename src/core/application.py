import sys
import pygame
from typing import Optional
from scenes import Scene
from constants import *

class Application:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(pygame.image.load(ICON_PATH))
        self.screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
        self.clock: pygame.Clock = pygame.Clock()
        self.scene: Optional[Scene] = None

    def run(self):
        while True:
            self.process()

    def quit(self):
        pygame.quit()
        sys.exit(0)

    def process(self):
        delta = self.clock.tick(FPS)
        self.process_events()

        if self.scene:
            self.scene.process(delta)

        pygame.display.update()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()

    def set_scene(self, scene: "Scene"):
        self.unload_scene()
        self.scene = scene(self)

    def unload_scene(self):
        if self.scene:
            self.scene = None
