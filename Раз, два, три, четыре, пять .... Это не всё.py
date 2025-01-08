def calculate_structure_sum(info):
    a = 0
    if isinstance(info, int) or isinstance(info, float):
        return info
    elif isinstance(info, str):
        return len(info)
    elif isinstance(info, list):
        for item in info:
            a += calculate_structure_sum(item)
        return a
    elif isinstance(info, tuple):
        for item in info:
            a += calculate_structure_sum(item)
        return a
    elif isinstance(info, set):
        for item in info:
            a += calculate_structure_sum(item)
        return a
    elif isinstance(info, dict):
        for key in info.items():
            a += calculate_structure_sum(key)

        return a
    else:
        return 0  # Возвращаем 0 для неподдерживаемых типов
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)