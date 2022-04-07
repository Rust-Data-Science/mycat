from logging import exception
from typing import Dict, Tuple, List

from ulist import UltraFastList
from . import errors as E


class DataFrame:
    """
    2D tabular data, which is the primary mycat data structure.
    Most of the methods are implemented for columns. The rows
    are ordered because the elements are stored in arrays.
    While the columns are not, for they are stored in a dict.
    """

    def __init__(self, data: Dict[str, UltraFastList]) -> None:
        self._data = data

    def __contains__(self, col: str) -> bool:
        """Whether self contains col.

        Args:
            col (str): Column name.

        Returns:
            bool
        """
        return col in self._data

    def __getitem__(self, col: str) -> UltraFastList:
        """Return the corresponding `ulist` object based on the
        given column name.

        Args:
            col (str): Column name.

        Raises:
            E.ColumnNotFoundError

        Returns:
            UltraFastList
        """
        result = self._data.get(col)
        if result is None:
            raise E.ColumnNotFoundError(col)
        return result

    def __setitem__(self, col: str, val: UltraFastList) -> None:
        """Add new column or modify existing column.

        Args:
            col (str): Column name.
            val (UltraFastList): Column value.
        """
        self._data[col] = val

    @property
    def columns(self) -> List[str]:
        """The column names of self."""
        return list(self._data.keys())

    @property
    def dtypes(self) -> Dict[str, str]:
        """The dtypes of self."""
        return {col: self[col].dtype for col in self.columns}

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

    def rename(self, cur: str, new: str) -> None:
        """Rename the column <cur> as <new>.

        Args:
            cur (str): Current column name.
            new (str): New column name.

        Raises:
            ValueError
            E.ColumnNotFoundError
        """
        if new in self:
            raise ValueError(f"The name '{new}' is in use.")
        if cur in self:
            self._data[new] = self._data.pop(cur)
        else:
            raise E.ColumnNotFoundError(cur)
