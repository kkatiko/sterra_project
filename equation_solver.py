import math
import cmath
import sys
import time
import re


def is_complex(s):
    pattern = r'^[+-]?\d*\.?\d+[+-]\d*\.?\d*[ij]$|^[+-]?\d*\.?\d*[ij]$'
    return bool(re.fullmatch(pattern, s.lower().replace(' ', '')))


def solve_quadratic_equation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                raise ValueError("Уравнение имеет бесконечное "
                                 "количество решений")
            else:
                raise ValueError("Уравнение не имеет решений")
        else:
            return (-c / b,)  # Линейное уравнение

    try:
        discriminant = b ** 2 - 4 * a * c
        if math.isinf(discriminant) or math.isnan(discriminant):
            raise ValueError("Коэффициенты слишком большие")
    except OverflowError:
        raise ValueError("Коэффициенты слишком большие")
    except TypeError:
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


def input_float(abc):
    last_interrupt_time = 0
    while True:
        try:
            value_str = input(abc)
            if value_str.lower() == 'inf':
                print("Ошибка: коэффициент не может быть бесконечностью. "
                      "Введите вещественное число.")
                continue

            if is_complex(value_str):
                print("Ошибка: введите вещественное число (без 'i' или 'j').")
                continue

            value = float(value_str)

            if math.isnan(value):
                print("Ошибка: введено значение nan. Попробуйте снова.")
                continue

            if math.isinf(value):
                print("Ошибка: коэффициент не может быть бесконечностью. "
                      "Введите вещественное число.")
                continue

            if not value_str.isascii():
                print("Ошибка: используйте стандартные цифры (0-9).")
                continue
            return value

        except ValueError:
            print("Ошибка: введите числовое значение.")

        except KeyboardInterrupt:
            current_time = time.time()
            # Двойное нажатие за 1 секунду
            if current_time - last_interrupt_time < 1.0:
                print("\nЭкстренное завершение программы.")
                sys.exit(0)
            else:
                print("\nДля выхода нажмите Ctrl+C ещё раз "
                      "в течении 1 секунды. Продолжаем ввод...")
                last_interrupt_time = current_time

        except Exception as e:
            print(f"Неожиданная ошибка: {e}. Пожалуйста, попробуйте снова.")
            continue


def main():
    print("Решение квадратного уравнения ax^2 + bx + c = 0")

    try:
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
    except KeyboardInterrupt:
        print("\nПрограмма была прервана пользователем. Завершение работы...")
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}. Завершение работы...")
        sys.exit(1)


if __name__ == "__main__":
    main()
