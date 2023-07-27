from __future__ import annotations

import abc

from game import BaseGame, AdminGame, ModeratorGame, ClientGame
from user import BaseUser, Admin, Moderator, Client


class BaseFactory(abc.ABC):
    @abc.abstractmethod
    def create_user(self) -> BaseUser: ...

    @abc.abstractmethod
    def create_game(self) -> BaseGame: ...


class ClientFactory(BaseFactory):
    def create_user(self) -> BaseUser:
        return Client(name='CLIENT Vlad')

    def create_game(self) -> BaseGame:
        return ClientGame()


class ModeratorFactory(BaseFactory):
    def create_user(self) -> BaseUser:
        return Moderator(name='MODERATOR Vlad')

    def create_game(self) -> BaseGame:
        return ModeratorGame()


class AdminFactory(BaseFactory):
    def create_user(self) -> BaseUser:
        return Admin(name='ADMIN Vlad')

    def create_game(self) -> BaseGame:
        return AdminGame()
