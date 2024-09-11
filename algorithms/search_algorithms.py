def linear_search(lst: list, num: int) -> int:
    for index, value in enumerate(lst):
        if value == num:
            return index
    return -1


def binary_search(lst: list, num: int):
    iteration = 0

    start = 0
    end = len(lst) - 1

    while end >= start:
        middle = (end + start) // 2
        iteration += 1

        if lst[middle] == num:
            return f"Found a {num} in {iteration} iterations"

        elif lst[middle] > num:
            end = middle - 1

        elif lst[middle] < num:
            start = middle + 1

    return f"{num} not found in the array"


def two_pointer_search_example(lst: list, target: int) -> tuple[int, int]:
    start = 0
    end = len(lst) - 1

    while start < end:
        current_sum = lst[start] + lst[end]

        if current_sum == target:
            return lst[start], lst[end]
        elif current_sum < target:
            start += 1
        else:
            end -= 1

    return -1, -1
