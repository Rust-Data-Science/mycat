"""
Test mutable methods.
"""

import mycat as mc
import ulist as ul
import pytest

ARR1 = ul.arange(3)
ARR2 = ul.from_seq([True, False, True], dtype='bool')


@pytest.mark.parametrize(
    'cur, new, is_exception',
    [
        ('foo', 'baz', False),
        ('foo', 'foo', True),
        ('foo', 'bar', True),
        ('baz', 'foo', True),
        ('baz', 'pie', True),
    ],
)
def test_rename(cur: str, new: str, is_exception: bool) -> None:
    df = mc.DataFrame(
        {
            'foo': ARR1,
            'bar': ARR2,
        }
    )
    if is_exception:
        with pytest.raises(Exception):
            df.rename(cur, new)
        assert df['foo'] is ARR1
    else:
        df.rename(cur, new)
        assert df[new] is ARR1
    assert df['bar'] is ARR2
    assert df.n_cols == 2
