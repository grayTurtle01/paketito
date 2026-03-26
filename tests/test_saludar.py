from paketito.modulo import saludar


def test_saludar_1():
    assert saludar() == "Hola desde paketito"
