
def is_multiple(n,m):
    return True if n%m == 0 else False


def mini_max(data):
    iter_seq = iter(data)
    next_value = next(iter_seq, None)
    max_val, min_val = next_value, next_value

    while next_value is not None:
        if max_val < next_value:
            max_val = next_value
        if min_val > next_value:
            min_val = next_value

        next_value = next(iter_seq, None)

    return min_val, max_val


def square_sum(n):


# print(is_multiple(27, 3))
# print(is_multiple(26, 3))
#
# print(divmod(26, 3))

print(mini_max([23, 42, 14, 4, 5, 18, 20]))

