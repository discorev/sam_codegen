import pathlib
from typing import Type, List
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader  # type: ignore

from .dialect import OpenAPIDialect, OpenAPIDialect30, OpenAPIDialect31
from .errors import OpenAPITemplateError

__all__ = ["OpenAPIFactory"]


# List out the supported dialects
supported_dialects: List[Type[OpenAPIDialect]] = [
    OpenAPIDialect30,
    OpenAPIDialect31,
]


class OpenAPIFactory:
    @classmethod
    def get(cls, template: str) -> OpenAPIDialect:
        _new = cls(template)
        return _new.get_dialect()

    def __init__(self, template_path: str):
        template = pathlib.Path(template_path)
        with template.open("r") as template_handle:
            self.data = load(template_handle, Loader=Loader)

    def template_version(self):
        if "openapi" not in self.data:
            return None
        version: str = self.data["openapi"]
        return tuple(
            int(part) if part.isdigit() else part
            for part in version.split(".", maxsplit=3)
        )

    def get_dialect(self) -> OpenAPIDialect:
        """Load the dialect for the template OpenAPI language."""
        version = self.template_version()
        if version is None:
            raise OpenAPITemplateError("Invalid or unsupported version")
        for dialect in supported_dialects:
            if version[:2] == dialect.api_version():
                return dialect(self.data)

        if version[:2] == OpenAPIDialect30.api_version():
            return OpenAPIDialect30(self.data)
        if version[:2] == (3, 1):
            return OpenAPIDialect31(self.data)
        raise OpenAPITemplateError("Invalid or unsupported version")
