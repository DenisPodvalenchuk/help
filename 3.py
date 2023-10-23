matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

max_val = float('-inf')  # инициализируем начальное максимальное значение как отрицательную бесконечность

for row in matrix:
    for i in range(0, len(row), 2):
        if row[i] > max_val:
            max_val = row[i]

print(f"Максимальное значение среди нечетных столбцов матрицы: {max_val}")