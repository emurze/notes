from __future__ import annotations
import abc
from random import random


class BaseGame(abc.ABC):
    @abc.abstractmethod
    def run(self) -> str: ...


class ClientGame(BaseGame):
    title = "Client Game"

    def run(self) -> bool:
        return bool(random())

    def __repr__(self) -> str:
        return self.title


class ModeratorGame(BaseGame):
    title = "Moderator Game"

    def run(self) -> bool:
        return bool(random())

    def __repr__(self) -> str:
        return self.title


class AdminGame(BaseGame):
    title = "Admin Game"

    def run(self) -> bool:
        return bool(random())

    def __repr__(self) -> str:
        return self.title
