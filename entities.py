from enum import Enum


class Direction(Enum):
    ...


class GhostMode(Enum):
    ...


class Entity:
    def __init__(self, name, power, x, y):
        self.x = x
        self.y = y
        ...

class Pacman(Entity):
    def __init__(self):
        self.lives = 3
        super().__init__(name="Pacman", power=1, x=0, y=0)
        self.score = 0

    def move(self):
        ...

    def eat(self):
        ...


class Ghost(Entity):
    def __init__(self):
        super().__init__(name="Ghost", power=1, x=0, y=0)

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
