def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [2, 'список', False]
print_params(*values_list)
values_dict = {'a': 3, 'b': 'словарь', 'c': True}
print_params(**values_dict)

values_list_2 = [5, 'параметры']
print_params(*values_list_2, 42)

values_list_3 = [54.32, 'Строка']
print_params(*values_list_3, 42)