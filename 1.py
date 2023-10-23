matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

max_val = float('-inf')  # инициализируем начальное максимальное значение как отрицательную бесконечность
min_val = float('inf')   # инициализируем начальное минимальное значение как положительную бесконечность

for row in matrix:
    for element in row:
        if element > max_val:
            max_val = element
        if element < min_val:
            min_val = element

print(f"Максимальное значение: {max_val}")
print(f"Минимальное значение: {min_val}")
