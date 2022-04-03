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
}


@pytest.mark.parametrize(
    'method, df, expected',
    [
        ('columns', 'df1', ['foo', 'bar']),
        ('empty', 'df1', False),
        ('shape', 'df1', (3, 2)),
        ('n_rows', 'df1', 3),
        ('n_cols', 'df1', 2),
    ],
)
def test(method: str, df: str, expected: Any) -> None:
    result = getattr(DATAFRAMES[df], method)()
    assert result == expected
