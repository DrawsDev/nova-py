from scenes import Scene

class Example(Scene):
    def ready(self):
        return
    
    def process(self, delta):
        if self.app.input.pressed("a"):
            self.app.quit()
