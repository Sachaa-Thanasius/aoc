import time
from typing import Self


class catchtime:
    """A small context manager to catch the time taken to execute its body."""

    def __enter__(self) -> Self:
        self.time = time.perf_counter()
        return self

    def __exit__(self, *args: object) -> None:
        self.time = time.perf_counter() - self.time
