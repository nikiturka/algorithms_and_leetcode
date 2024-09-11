def factorial(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    return factorial(num - 1) * num


def fibonacci_search(num: int) -> int:
    if num == 1:
        return 1
    if num == 0:
        return 0
    return fibonacci_search(num - 1) + fibonacci_search(num - 2)
