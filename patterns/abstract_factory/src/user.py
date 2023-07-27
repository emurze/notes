from __future__ import annotations
import abc
from dataclasses import dataclass


class BaseUser(abc.ABC):
    @abc.abstractmethod
    def get_name(self) -> str: ...


@dataclass(frozen=True)
class Client(BaseUser):
    name: str

    def get_name(self) -> str:
        return self.name


@dataclass(frozen=True)
class Moderator(BaseUser):
    name: str

    def get_name(self) -> str:
        return self.name


@dataclass(frozen=True)
class Admin(BaseUser):
    name: str

    def get_name(self) -> str:
        return self.name