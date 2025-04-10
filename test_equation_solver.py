import pytest
import cmath
import math
from equation_solver import solve_quadratic_equation

def test_basic_cases(test_cases):
    # тест верных случаев через test_cases
    for case in test_cases.values():
        a, b, c, expected = case
        result = solve_quadratic_equation(a, b, c)
        if isinstance(expected[0], complex):
            assert cmath.isclose(result[0], expected[0], rel_tol=1e-9)
            assert cmath.isclose(result[1], expected[1], rel_tol=1e-9)
        else:
            assert result == expected

def test_error_cases(error_cases):
    # тест возникающих ошибок через error_cases
    for case in error_cases:
        a, b, c, msg = case
        with pytest.raises(ValueError, match=msg):
            solve_quadratic_equation(a, b, c)

@pytest.mark.parametrize("a,b,c,expected", [
    (1, 0, -1, (1.0, -1.0)),  # x² - 1 = 0
    (1, 0, -4, (2.0, -2.0)),  # x² - 4 = 0
    (1, 0, 0, (0.0,)),        # x² = 0
])
def test_no_linear_term(a, b, c, expected):
    # тест для случаев, где нет линейного коэффициента
    assert solve_quadratic_equation(a, b, c) == expected

def test_very_small_coefficients():
    # очень маленькие коэффициенты
    roots = solve_quadratic_equation(1e-20, 2e-20, 1e-20)
    assert math.isclose(roots[0], -1.0, rel_tol=1e-9)
