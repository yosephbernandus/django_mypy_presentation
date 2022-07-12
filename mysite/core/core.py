from typing import Callable


def foo(x: int) -> Callable:
    def bar(y: int) -> str:
        return f"In bar, {x} * {y} = {x*y}"
    return bar
