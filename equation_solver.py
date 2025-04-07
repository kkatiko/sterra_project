import math
import cmath


def solve_quadratic_equation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                raise ValueError("Уравнение имеет бесконечное количество решений")
            else:
                raise ValueError("Уравнение не имеет решений")
        else:
            return (-c / b,)  # Линейное уравнение

    try:
        discriminant = b ** 2 - 4 * a * c
        if math.isinf(discriminant) or math.isnan(discriminant):
            raise ValueError("Коэффициенты слишком большие")
    except (TypeError, OverflowError):
        raise ValueError("Коэффициенты не подходят")

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        # Комплексные корни
        x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return x1, x2


def format_complex(z):
    # Форматирование комплексного числа
    if z.imag == 0:
        return f"{z.real}"
    elif z.real == 0:
        return f"{z.imag}j"
    else:
        return f"{z.real} + {z.imag}j"


def input_float(prompt):
    # Ввод с проверкой на числовое значение
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка: введите числовое значение.")


def main():
    print("Решение квадратного уравнения ax^2 + bx + c = 0")

    a = input_float("Введите коэффициент a: ")
    b = input_float("Введите коэффициент b: ")
    c = input_float("Введите коэффициент c: ")

    try:
        roots = solve_quadratic_equation(a, b, c)
        if not roots:
            print("Уравнение не имеет корней.")
        elif len(roots) == 1:
            print("Уравнение имеет один корень: x =", roots[0])
        else:
            x1, x2 = roots
            if isinstance(x1, complex):
                print("Уравнение имеет два комплексных корня:")
                print("x1 =", format_complex(x1))
                print("x2 =", format_complex(x2))
            else:
                print("Уравнение имеет два корня:")
                print("x1 =", x1)
                print("x2 =", x2)
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()