import pytest
import numpy as np


@pytest.fixture
def test_cases():
    # тестовые данные для верных случаев
    return {
        'two_real': (1, -3, 2, (2.0, 1.0)),
        'one_real': (1, -2, 1, (1.0,)),
        'complex': (1, 2, 5, (-1+2j, -1-2j)),
        'linear': (0, 2, -4, (2.0,))
    }


@pytest.fixture
def error_cases():
    # тестовые данные для проверки возникающих ошибок
    return [
        (0, 0, 5, "Уравнение не имеет решений"),
        (0, 0, 0, "Уравнение имеет бесконечное количество решений"),
        (1e308, 1e308, 1e308, "Коэффициенты слишком большие"),
        ('a', 1, 2, "Коэффициенты не подходят"),
        (1, 'b', 2, "Коэффициенты не подходят"),
        (1, 2, 'c', "Коэффициенты не подходят")
    ]


# ------------------------------------------------------------
# Генерация случайных коэффициентов
@pytest.fixture
def random_coeffs():
    np.random.seed(42)
    # a, b, c
    return np.random.uniform(-10, 10, size=3)


@pytest.fixture()
def np_solver():
    def solve_np(a, b, c):
        coeffs = [a, b, c]
        roots = np.roots(coeffs)
        return roots
    return solve_np
