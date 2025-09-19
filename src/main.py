from core import Application
from scenes import Example

if __name__ == "__main__":
    applicaition = Application()
    applicaition.set_scene(Example)
    applicaition.run()
