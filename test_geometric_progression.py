import pytest
from geometric_progression import calc_geom_prg


def test_geoemtric_progression():
    init = 1
    ratio = 2
    exponent = 40
    expected_result = init*ratio**exponent
    actual_result = calc_geom_prg(init,ratio,exponent)
    assert expected_result == actual_result

def test_geoemtric_progression_with_non_integer_exponent():
    init = 1
    ratio = 2
    exponent = 40.1
    expected_result = "number of iteration must be an integer"
    actual_result = calc_geom_prg(init, ratio, exponent)
    assert expected_result == actual_result
