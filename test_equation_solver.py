import pytest
import cmath
import math
from equation_solver import solve_quadratic_equation
import numpy as np
import mpmath
import sympy
from scipy import optimize


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


# -----------------------------------------------------------
def test_with_numpy(random_coeffs):
    # Сравнение с numpy и фикстурой с рандомными коэффицентами
    a, b, c = random_coeffs
    numpy_roots = np.roots([a, b, c])
    our_roots = solve_quadratic_equation(a, b, c)
    assert np.allclose(sorted(our_roots), sorted(numpy_roots))


@pytest.mark.parametrize("lib", [np, mpmath, sympy, optimize])
def test_multiple_libs(lib):
    # тест с использованием разных библиотек
    a, b, c = 1, -5, 6  # x² -5x +6 =0 → корни 2 и 3
    if lib == sympy:
        x = sympy.symbols('x')
        sympy_roots = sympy.solve(a * x ** 2 + b * x + c, x)
        expected = [float(r) for r in sympy_roots]
    elif lib == optimize:  # Обработка SciPy
        def equation(x):
            return a * x ** 2 + b * x + c

        sol1 = optimize.root(equation, x0=0).x[0]
        sol2 = optimize.root(equation, x0=5).x[0]
        expected = [sol1, sol2]
    elif hasattr(lib, 'roots'):
        expected = lib.roots([a, b, c])
    else:
        expected = [2, 3]

    result = solve_quadratic_equation(a, b, c)
    assert np.allclose(sorted(result), sorted(expected))


def test_np_solver_complex_roots(np_solver):
    # Тест на комплексные корни с numpy
    # x^2 + 2x + 5 = 0, корни -1+2j и -1-2j
    a, b, c = 1, 2, 5
    roots = np_solver(a, b, c)
    expected_root1 = -1 + 2j
    expected_root2 = -1 - 2j
    # numpy может возвращать корни в разном порядке,
    # поэтому проверяется наличие каждого из них
    assert (np.isclose(roots[0], expected_root1).any()
            or np.isclose(roots[0], expected_root2).any())
    assert (np.isclose(roots[1], expected_root1).any()
            or np.isclose(roots[1], expected_root2).any())


def test_np_solver_single_real_root(np_solver):
    # Тест на один действительный корень с numpy
    a, b, c = 1, -4, 4  # x^2 - 4x + 4 = 0, корень 2
    roots = np_solver(a, b, c)
    # Проверяем, что один из корней равен 2
    assert np.isclose(roots[0], 2).any()
    # Если numpy вернул два корня
    if len(roots) > 1:
        assert np.isclose(roots[1], 2).any()


def test_np_solver_linear_equation(np_solver):
    # Тест для линейного уравнения c numpy
    a, b, c = 0, 2, -4  # 2x - 4 = 0, корень 2
    roots = np_solver(a, b, c)
    assert np.isclose(roots[0], 2).any()
