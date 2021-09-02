from typing import Any
from itertools import chain
from pandas import (
    set_option,
    option_context,
)


def set_options(options: dict[str: Any]):
    for _ in options.items():
        set_option(*_)


def set_option_context(options: dict[str: Any]) -> option_context:
    return option_context(*chain.from_iterable(options.items()))
