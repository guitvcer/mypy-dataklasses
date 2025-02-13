from typing import Callable

from mypy.nodes import Argument, Var, ArgKind
from mypy.plugin import ClassDefContext, Plugin
from mypy.plugins.common import add_method_to_class
from mypy.types import NoneType


class DataklassesPlugin(Plugin):
    def get_class_decorator_hook(
        self, fullname: str
    ) -> Callable[[ClassDefContext], None] | None:
        if fullname == "main.dataklass":
            return _class_decorator_hook

        return None


def _class_decorator_hook(ctx: ClassDefContext) -> None:
    args = [
        Argument(
            variable=Var(name=name, type=node.type),
            type_annotation=node.type,
            initializer=None,
            kind=ArgKind.ARG_POS,
        )
        for name, node in ctx.cls.info.names.items()
    ]
    add_method_to_class(
        ctx.api,
        ctx.cls,
        "__init__",
        args=args,
        return_type=NoneType(),
    )

    # TODO: __repr__
    # TODO: __eq__
    # TODO: __match_args__


def plugin(version: str) -> type[DataklassesPlugin]:
    return DataklassesPlugin
