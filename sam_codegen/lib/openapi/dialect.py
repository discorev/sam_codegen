from abc import ABC, abstractclassmethod
from typing import Tuple


class OpenAPIDialect(ABC):
    def __init__(self, template) -> None:
        self.template = template

    @property
    def title(self) -> str:
        """Returns the API Title."""
        return self.template["info"]["title"]

    @property
    def description(self) -> str:
        """Returns the API Description."""
        return self.template["info"]["description"]

    @property
    def version(self) -> str:
        """Returns the API Version."""
        return self.template["info"]["version"]

    @classmethod
    @abstractclassmethod
    def api_version(cls) -> Tuple[int, int]:
        pass


class OpenAPIDialect30(OpenAPIDialect):
    @classmethod
    def api_version(cls) -> Tuple[int, int]:
        return (3, 0)


class OpenAPIDialect31(OpenAPIDialect):
    @classmethod
    def api_version(cls) -> Tuple[int, int]:
        return (3, 1)
