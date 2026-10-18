from enum import Enum


class Direction(Enum):
    ...


class GhostMode(Enum):
    ...


class Entity:
    def __init__(self, name, power):
        ...


class Pacman(Entity):
    def __init__(self):
        self.lives = 3
        super().__init__()

    def move(self):
        ...

    def eat(self):
        ...


class Ghost(Entity):
    def __init__(self):
        super().__init__()

    def chase(self):
        # bfs
        ...

    def run_away(self):
        ...

    def return_home(self):
        ...

    def freeze(self):
        ...

    def idle(self):
        ...


class PacGum(Entity):
    ...


class SuperGum(Entity):
    ...
