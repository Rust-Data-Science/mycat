from typing import Dict, Tuple, List

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

    @property
    def columns(self) -> List[str]:
        """The column labels of self."""
        return list(self._data.keys())

    @property
    def empty(self) -> bool:
        """Whether self is empty."""
        if self.n_cols == 0 or self.n_rows == 0:
            return True
        return False 

    @property
    def shape(self) -> Tuple[int, int]:
        """The dimensionality of self."""
        return (self.n_rows, self.n_cols)

    @property
    def n_rows(self) -> int:
        """The number of rows in self."""
        if self.n_cols == 0:
            return 0
        return len(list(self._data.values())[0])

    @property
    def n_cols(self) -> int:
        """The number of columns in self."""
        return len(self._data)
