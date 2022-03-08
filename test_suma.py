import pytest
from calc import suma, escribir


# Run Test | Debug Test
def test_suma():
    assert suma(2, 2) == 4


@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [(3, 2, 5), (2, 3, 5), (suma(3, 2), 5, 10), (3, suma(5, 2), 10)],
)
def test_suma_multi(input_a, input_b, expected):
    assert suma(input_a, input_b) == expected


def test_tmp_dir(tmpdir):
    data_in = "Prueba Pytest"
    fpath = f"{tmpdir}/test.txt"
    escribir(fpath, data_in)

    with open(fpath) as file_out:
        data_out = file_out.read()

    assert data_in == data_out
