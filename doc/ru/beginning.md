# Начало

## Описание

`Nova-py` - это фреймворк, использующий в своей основе библиотеку Pygame Community Edition. В первую очередь, он создавался и создаётся для реализации моего проекта для колледжа - [Answers Time](https://github.com/DrawsDev/answers-time).

> [!IMPORTANT]
> Требования:
> - Python 3.8.10
> - Библиотеки, перечисленные в файле `requirements.txt`. 

> [!IMPORTANT]
> Этот фреймворк может быть неэффективным. Если Вас это не останавливает, то в данной документации постараюсь описать фреймворк.

## Инициализация приложения

```py
from core import Application
from scenes import Example

if __name__ == "__main__":
    application = Application()    # Создание нового приложения
    application.set_scene(Example) # Установка Example как текущей сцены 
    application.run()              # Запуск приложения
```
> [!NOTE]
> В данном примере, инициализация нового приложения происходит в `main.py`.

#### Следующий раздел
- [Application](application.md)
