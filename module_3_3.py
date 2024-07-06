def  print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [2, "No", 1.5]
values_dict = {'a': 716, 'b': 772, 'c': 773}
values_list_2 = [78, 'Python']

print_params(*values_list_2, 42)