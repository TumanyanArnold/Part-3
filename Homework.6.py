def all_summ(sum_):
    total = 0

    if isinstance(sum_, (int, float)):
        return sum_
    elif isinstance(sum_, str):
        return len(sum_)
    elif isinstance(sum_, (list, set, tuple)):
        for i in sum_:
            total += all_summ(i)
    elif isinstance(sum_, object):
        for key, value in sum_.items():
            total += all_summ(key)
            total += all_summ(value)

    return total


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = all_summ(data_structure)
print(result)
