from core import Application
from scenes import Example

if __name__ == "__main__":
    application = Application()
    application.set_scene(Example)
    application.run()
