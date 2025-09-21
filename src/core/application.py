import sys
import pygame
from typing import Optional
from scenes import Scene
from .input import Input
from .window import Window
from constants import *

class Application:
    def __init__(self):
        pygame.init()
        self.window: Window = Window(TITLE, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.input: Input = Input()
        self.scene: Optional[Scene] = None
        self.window.set_icon(pygame.image.load(ICON_PATH))
        self.window.set_framerate(FRAMERATE)

    def run(self):
        while not self.window.should_close():
            self.process()
        self.quit()

    def quit(self):
        pygame.quit()
        sys.exit(0)

    def process(self):
        self.window.process()
        if self.scene:
            self.scene.process(self.window.get_delta())
        if self.input.just_pressed(pygame.K_F11):
            self.window.toggle_fullscreen()
    
    def set_scene(self, scene: "Scene"):
        self.unload_scene()
        self.scene = scene(self)

    def unload_scene(self):
        if self.scene:
            self.scene = None
