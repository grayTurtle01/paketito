from paketito.modulo import suma


def test_suma_1():
    assert suma(1, 1) == 2


def test_suma_2():
    assert suma(1, 0) == 1


def test_suma_3():
    assert suma(1, -1) == 0


def test_suma_4():
    assert suma(-1, -1) == -2
