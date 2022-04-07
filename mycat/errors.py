"""
Custom exceptions for mycat.
"""


class ColumnNotFoundError(KeyError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.col_name = args[0]

    def __str__(self) -> str:
        return f"Column '{self.col_name}' not found!"
