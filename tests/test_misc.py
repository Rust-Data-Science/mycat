"""
Unit tests which cannot be classified.
"""

import mycat as mc
import pathlib


def test_ver() -> None:
    """All the versions should be the same."""
    def _parse_setup_ver(line: str) -> str:
        for s in ["'", '"', "\n", " ", "=", "version"]:
            line = line.replace(s, "")
        return line

    root = pathlib.Path(__file__).parent.parent.resolve()
    setup_ver = ""
    with open(root / "setup.py") as f:
        for line in f:
            if line.startswith("version = "):
                setup_ver = _parse_setup_ver(line)
                break
    lib_ver = mc.__version__
    assert lib_ver == setup_ver
