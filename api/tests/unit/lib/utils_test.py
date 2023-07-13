import pytest
from src.verdantech_api.lib.utils import key_generator, read_file_async


@pytest.mark.parametrize(["length", "string"], [(10, "abcdefg"), (5, "aT$*tf@g")])
def test_key_generator(length: int, string: str):
    key = key_generator(size=length, chars=string)

    assert len(key) == length
    for char in key:
        assert char in string
