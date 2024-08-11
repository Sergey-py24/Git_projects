

def fibonacci_set(number):
    """Генерирует набор чисел Фибоначчи вплоть до заданного числа.

    Args:
        number: Верхний предел для чисел Фибоначчи

    Returns:
        Набор, содержащий числа Фибоначчи, меньшие или равные "number".
    """
    fib_set = {0, 1}  # Инициализация первых двух чисел Фибоначчи,
    a, b = 0, 1
    while b <= number:
        fib_set.add(b)
        a, b = b, a + b
    return fib_set

number = int(input())
result = list(fibonacci_set(number))
result = sorted(result)
print(result)

