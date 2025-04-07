import pytest
import cmath
from equation_solver import solve_quadratic_equation

def test_two_real_roots():
    # Два действительных корня x² - 3x + 2 = 0)
    roots = solve_quadratic_equation(1, -3, 2)
    assert roots == (2.0, 1.0)

def test_one_real_root():
    # Один действительный корень (x² - 2x + 1 = 0)
    roots = solve_quadratic_equation(1, -2, 1)
    assert roots == (1.0,)

def test_large_coefficients():
        with pytest.raises(ValueError, match="Коэффициенты не подходят"):
            solve_quadratic_equation(1e308, 1e308, 1e308)

def test_extremely_large_coefficients():
    with pytest.raises(ValueError, match="Коэффициенты слишком большие"):
        solve_quadratic_equation(2e308, 2e308, 2e308)


def test_complex_roots():
    # Комплексные корни (x² + 2x + 5 = 0)
    roots = solve_quadratic_equation(1, 2, 5)
    expected_root1 = -1 + 2j
    expected_root2 = -1 - 2j
    assert cmath.isclose(roots[0], expected_root1, rel_tol=1e-9)
    assert cmath.isclose(roots[1], expected_root2, rel_tol=1e-9)

def test_linear_equation():
    # Линейное уравнение (0x² + 2x - 4 = 0 → x = 2)
    roots = solve_quadratic_equation(0, 2, -4)
    assert roots == (2.0,)

def test_no_solution():
    # Вырожденный случай (0x² + 0x + 5 = 0)
    with pytest.raises(ValueError, match="Уравнение не имеет решений"):
        solve_quadratic_equation(0, 0, 5)

def test_infinite_solutions():
    # Бесконечное количество решений (0x² + 0x + 0 = 0)
    with pytest.raises(ValueError, match="Уравнение имеет бесконечное количество решений"):
        solve_quadratic_equation(0, 0, 0)

def test_invalid_coefficient_a():
    with pytest.raises(ValueError, match="Коэффициенты не подходят"):
        solve_quadratic_equation('a', 1, 2)

def test_invalid_coefficients_b():
    with pytest.raises(ValueError, match="Коэффициенты не подходят"):
        solve_quadratic_equation(1, 'j', 2)

def test_invalid_coefficients_c():
    with pytest.raises(ValueError, match="Коэффициенты не подходят"):
        solve_quadratic_equation(3, 1, '/')

def test_invalid_coefficients():
    with pytest.raises(ValueError, match="Коэффициенты не подходят"):
        solve_quadratic_equation('g', 'f', '/')
