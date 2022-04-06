"""
Unit tests for the DataFrame information methods.
"""

import mycat as mc
import ulist as ul
import pytest
from typing import Any

DATAFRAMES = {
    'df1': mc.DataFrame(
        {
            'foo': ul.arange(3),
            'bar': ul.from_seq([True, False, True], dtype='bool'),
        }
    ),
    'df2': mc.DataFrame(dict()),
    'df3': mc.DataFrame(
        {
            'foo': ul.from_seq([], dtype='int'),
            'bar': ul.from_seq([], dtype='bool'),
        }
    ),
}


@pytest.mark.parametrize(
    'method, df, expected',
    [
        ('columns', 'df1', ['foo', 'bar']),
        ('columns', 'df2', []),
        ('columns', 'df3', ['foo', 'bar']),

        ('dtypes', 'df1', {'foo': 'int64', 'bar': 'bool'}),
        ('dtypes', 'df2', dict()),
        ('dtypes', 'df3', {'foo': 'int64', 'bar': 'bool'}),

        ('empty', 'df1', False),
        ('empty', 'df2', True),
        ('empty', 'df3', True),

        ('shape', 'df1', (3, 2)),
        ('shape', 'df2', (0, 0)),
        ('shape', 'df3', (0, 2)),

        ('n_rows', 'df1', 3),
        ('n_rows', 'df2', 0),
        ('n_rows', 'df3', 0),

        ('n_cols', 'df1', 2),
        ('n_cols', 'df2', 0),
        ('n_cols', 'df3', 2),
    ],
)
def test(method: str, df: str, expected: Any) -> None:
    obj = getattr(DATAFRAMES[df], method)
    if callable(obj):
        result = obj()
    else:
        result = obj
    assert result == expected
