# benefits
#
# Modularity - break apart your problem into small pieces.
# Composability - lots of function that could be combined.
# Ease of debugging and testing.


def square(value: int) -> int:
    return value ** 2


def calc_sum(a: int, b: int) -> int:
    return a + b


def main():
    a, b = 2, 3
    my_sum = calc_sum(a, b)
    my_square = square(my_sum)
    print(my_square)

    # functional way
    # print(square(calc_sum(5, 7)))


main()
