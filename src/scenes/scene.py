from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core import Application

class Scene:
    def __init__(self, app: "Application"):
        self.app: "Application" = app
        self.ready()
    
    def ready(self):
        pass

    def process(self, delta: float):
        pass
