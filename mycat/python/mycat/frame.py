from typing import Dict

from ulist import UltraFastList


class DataFrame:
    """
    2D tabular data, which is the primary mycat data structure.
    Most of the methods are implemented for columns. The rows
    are ordered because the elements are stored in arrays.
    While the columns are not, for they are stored in a dict.
    """

    def __init__(self, data: Dict[str, UltraFastList]) -> None:
        self._data = data
