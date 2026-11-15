import pytest

from main import kali, kurang, tambah


def test_tambah():
    assert tambah(1, 2) == 3


def test_kurang():
    assert kurang(5, 3) == 2


@pytest.mark.parametrize(
    ("a", "b", "hasil"),
    [
        (2, 3, 6),
        (-2, 3, -6),
        (0, 100, 0),
    ],
)
def test_kali(a, b, hasil):
    assert kali(a, b) == hasil
