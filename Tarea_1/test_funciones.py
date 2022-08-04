from Tarea_1.funciones import basic_operations
from Tarea_1.funciones import count_char


def test_operations():
    assert basic_operations(2, 3, 1) == 5
    assert basic_operations(5, 3, 2) == 2
    assert basic_operations(8, 2, 3) == 4


def test_opstr():
    assert basic_operations("hola", 2, 3) == 420
    assert basic_operations(2, "hola", 3) == 420
    assert basic_operations(2, 3, "hola") == 420


def test_div0():
    assert basic_operations(2, 0, 3) == 3312


def test_count_char():
    assert count_char("roma") == 4


def test_no_str():
    assert count_char(3) == 1314
