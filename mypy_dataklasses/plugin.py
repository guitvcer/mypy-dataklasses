from typing import Callable

from mypy.nodes import Argument, Var, ArgKind
from mypy.plugin import ClassDefContext, Plugin
from mypy.plugins.common import add_attribute_to_class, add_method_to_class
from mypy.types import NoneType


class DataklassesPlugin(Plugin):
    def get_class_decorator_hook(
        self, fullname: str
    ) -> Callable[[ClassDefContext], None] | None:
        if fullname == "main.dataklass":
            return _class_decorator_hook

        return None


def _class_decorator_hook(ctx: ClassDefContext) -> None:
    init_args = [
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
        args=init_args,
        return_type=NoneType(),
    )

    add_method_to_class(
        ctx.api,
        ctx.cls,
        "__repr__",
        args=[],
        return_type=ctx.api.named_type("builtins.str"),
    )

    add_method_to_class(
        ctx.api,
        ctx.cls,
        "__eq__",
        args=[
            Argument(
                variable=Var(name="other", type=ctx.api.named_type(ctx.cls.fullname)),
                type_annotation=ctx.api.named_type(ctx.cls.fullname),
                initializer=None,
                kind=ArgKind.ARG_POS,
            ),
        ],
        return_type=ctx.api.named_type("builtins.bool"),
    )

    add_attribute_to_class(
        ctx.api,
        ctx.cls,
        "__match_args__",
        typ=ctx.api.named_type(
            "builtins.tuple", args=[ctx.api.named_type("builtins.str")]
        ),
    )


def plugin(version: str) -> type[DataklassesPlugin]:
    return DataklassesPlugin
