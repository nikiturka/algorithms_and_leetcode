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


# Reverse list in O(1)
def two_pointer_search_example(lst: list) -> list:
    start, finish = 0, len(lst) - 1

    while start < finish:
        lst[start], lst[finish] = lst[finish], lst[start]
        start += 1
        finish -= 1

    return lst
