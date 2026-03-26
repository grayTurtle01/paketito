from paketito.modulo import resta


def test_resta_1():
    assert resta(1, 1) == 0


def test_resta_2():
    assert resta(1, 0) == 1


def test_resta_3():
    assert resta(1, -1) == 2


def test_resta_4():
    assert resta(-1, -1) == 0
